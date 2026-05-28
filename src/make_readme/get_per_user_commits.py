import json
import logging
import os
import tempfile
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import requests

try:
    from .github_api import (
        is_critical_api_error,
        log_noncritical_api_error,
        raise_api_error,
    )
except ImportError:
    from github_api import (
        is_critical_api_error,
        log_noncritical_api_error,
        raise_api_error,
    )

# Replace these with your GitHub token and organization name
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable not set")
ORG_NAME = "CCBR"
# ORG_NAME = 'CCRGeneticsBranch'
# ORG_NAME = 'NIDAP-Community'
# ORG_NAME = 'NCI-VB'

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}",
}

logger = logging.getLogger(__name__)

STATE_SCHEMA_VERSION = 2


def get_default_state_file_path():
    state_path_override = os.getenv("PER_USER_COMMITS_STATE_PATH")
    if state_path_override:
        return Path(state_path_override).expanduser().resolve()

    cache_root = os.getenv("XDG_CACHE_HOME")
    if cache_root:
        cache_base = Path(cache_root).expanduser()
    else:
        cache_base = Path(tempfile.gettempdir()) / "ccbr_cache"

    return cache_base / "per_user_commits_state.json"


STATE_FILE_PATH = get_default_state_file_path()


def initialize_state():
    return {
        "schema_version": STATE_SCHEMA_VERSION,
        "updated_at": None,
        "repos": {},
        "commit_metadata": {},
    }


def load_state(state_path=STATE_FILE_PATH):
    if not state_path.exists():
        return initialize_state()

    try:
        with state_path.open("r", encoding="utf-8") as fh:
            state = json.load(fh)
    except (OSError, json.JSONDecodeError) as error:
        logger.warning(
            "Failed to read state file %s (%s). Rebuilding state from scratch.",
            state_path,
            error,
        )
        return initialize_state()

    if state.get("schema_version") != STATE_SCHEMA_VERSION:
        logger.warning(
            "State file schema mismatch in %s. Rebuilding state from scratch.",
            state_path,
        )
        return initialize_state()

    if not isinstance(state.get("repos"), dict) or not isinstance(
        state.get("commit_metadata"), dict
    ):
        logger.warning(
            "State file %s is missing required keys. Rebuilding state from scratch.",
            state_path,
        )
        return initialize_state()

    return state


def save_state(state, state_path=STATE_FILE_PATH):
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    temp_path = state_path.with_suffix(".tmp")
    with temp_path.open("w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2, sort_keys=True)
    temp_path.replace(state_path)


def parse_commit_date(commit_date_str):
    return datetime.strptime(commit_date_str, "%Y-%m-%dT%H:%M:%SZ")


def get_commit_author_login(commit):
    if commit.get("author") and commit["author"].get("login"):
        return commit["author"]["login"]
    return None


def get_commit_date(commit):
    commit_author = commit.get("commit", {}).get("author", {})
    return commit_author.get("date")


def record_commit_metadata(commit, commit_metadata):
    sha = commit.get("sha")
    author_login = get_commit_author_login(commit)
    commit_date = get_commit_date(commit)

    if not sha or not author_login or not commit_date:
        return None

    commit_metadata[sha] = {"author": author_login, "date": commit_date}
    return sha


def get_repos(org_name):
    repos = []
    page = 1
    has_more_pages = True
    while has_more_pages:
        response = requests.get(
            f"https://api.github.com/orgs/{org_name}/repos?per_page=100&page={page}",
            headers=headers,
        )
        if response.status_code != 200:
            raise_api_error(response, f"repositories for org '{org_name}'")
        page_repos = response.json()
        repos.extend(page_repos)
        has_more_pages = len(page_repos) == 100
        if has_more_pages:
            page += 1
    if not repos:
        raise RuntimeError(
            f"No repositories were returned for org '{org_name}'. "
            "Critical README data is unavailable. "
            "Check whether GITHUB_TOKEN is expired or missing required permissions."
        )
    return repos


def get_members(org_name):
    members = set()
    page = 1
    has_more_pages = True
    while has_more_pages:
        response = requests.get(
            f"https://api.github.com/orgs/{org_name}/members?per_page=100&page={page}",
            headers=headers,
        )
        if response.status_code != 200:
            raise_api_error(response, f"members for org '{org_name}'")
        page_members = response.json()
        has_more_pages = bool(page_members)
        for member in page_members:
            members.add(member["login"])
        if has_more_pages:
            page += 1
    if not members:
        raise RuntimeError(
            f"No members were returned for org '{org_name}'. "
            "Critical README data is unavailable. "
            "Check whether GITHUB_TOKEN is expired or missing required permissions."
        )
    return members


def get_repo_branch_tips(repo_full_name):
    branch_tips = {}
    page = 1
    has_more_pages = True

    while has_more_pages:
        response = requests.get(
            f"https://api.github.com/repos/{repo_full_name}/branches?per_page=100&page={page}",
            headers=headers,
        )
        if response.status_code != 200:
            if is_critical_api_error(response):
                raise_api_error(response, f"branches for repo '{repo_full_name}'")
            log_noncritical_api_error(
                response,
                f"branches for repo '{repo_full_name}'",
                "cached branch data for that repository",
                logger,
            )
            return None

        page_branches = response.json()
        has_more_pages = bool(page_branches)
        for branch in page_branches:
            branch_name = branch.get("name")
            branch_sha = branch.get("commit", {}).get("sha")
            if branch_name and branch_sha:
                branch_tips[branch_name] = branch_sha

        if has_more_pages:
            page += 1

    return branch_tips


def get_branch_commits_full(
    repo_full_name, branch_name, commit_metadata
):
    branch_shas = set()
    page = 1
    has_more_pages = True

    while has_more_pages:
        response = requests.get(
            f"https://api.github.com/repos/{repo_full_name}/commits",
            params={"sha": branch_name, "per_page": 100, "page": page},
            headers=headers,
        )
        if response.status_code != 200:
            if is_critical_api_error(response):
                raise_api_error(
                    response,
                    f"commits for repo '{repo_full_name}' branch '{branch_name}'",
                )
            log_noncritical_api_error(
                response,
                f"commits for repo '{repo_full_name}' branch '{branch_name}'",
                "cached branch commit data",
                logger,
            )
            return None

        commits = response.json()
        has_more_pages = bool(commits)
        for commit in commits:
            sha = record_commit_metadata(commit, commit_metadata)
            if sha:
                branch_shas.add(sha)

        if has_more_pages:
            page += 1

    return branch_shas


def get_compare_data(repo_full_name, base_sha, head_sha):
    response = requests.get(
        f"https://api.github.com/repos/{repo_full_name}/compare/{base_sha}...{head_sha}",
        headers=headers,
    )
    if response.status_code != 200:
        if is_critical_api_error(response):
            raise_api_error(
                response,
                f"compare for repo '{repo_full_name}' ({base_sha}...{head_sha})",
            )
        log_noncritical_api_error(
            response,
            f"compare for repo '{repo_full_name}' ({base_sha}...{head_sha})",
            "full branch resync",
            logger,
        )
        return None

    return response.json()


def aggregate_user_counts(active_shas, commit_metadata, eligible_members):
    user_commits = defaultdict(
        lambda: {"total": 0, "last_month": 0, "last_6_months": 0}
    )

    today = datetime.utcnow()
    one_month_ago = today - timedelta(days=30)
    six_months_ago = today - timedelta(days=180)

    for sha in active_shas:
        metadata = commit_metadata.get(sha)
        if not metadata:
            continue
        author = metadata.get("author")
        commit_date_str = metadata.get("date")
        if not author or not commit_date_str:
            continue
        if author not in eligible_members:
            continue

        try:
            commit_date = parse_commit_date(commit_date_str)
        except ValueError:
            logger.warning(
                "Skipping commit %s due to invalid cached date format: %s",
                sha,
                commit_date_str,
            )
            continue
        user_commits[author]["total"] += 1
        if commit_date >= one_month_ago:
            user_commits[author]["last_month"] += 1
        if commit_date >= six_months_ago:
            user_commits[author]["last_6_months"] += 1

    return user_commits


def get_per_user_commits(
    include_all_branches=False,
    include_archived=True,
    include_forks=True,
    use_cache=True,
    log_run_summary=True,
):
    members = get_members(ORG_NAME)
    repos = get_repos(ORG_NAME)

    run_stats = {
        "repos_total": len(repos),
        "repos_processed": 0,
        "repos_skipped_archived": 0,
        "repos_skipped_forks": 0,
        "repos_branch_tip_failures": 0,
        "repos_reused_cached_on_tip_failure": 0,
        "branches_seen": 0,
        "branch_cache_hits": 0,
        "branch_compare_attempts": 0,
        "branch_compare_delta_applied": 0,
        "branch_compare_resync_required": 0,
        "branch_full_resync_attempts": 0,
        "branch_full_resync_success": 0,
        "branch_full_resync_fallback_cached": 0,
        "branch_full_resync_empty": 0,
        "delta_commits_added": 0,
    }

    state = load_state() if use_cache else initialize_state()
    commit_metadata = dict(state.get("commit_metadata", {}))

    next_repos_state = {}

    for repo in repos:
        if not include_archived and repo.get("archived", False):
            run_stats["repos_skipped_archived"] += 1
            continue
        if not include_forks and repo.get("fork", False):
            run_stats["repos_skipped_forks"] += 1
            continue

        run_stats["repos_processed"] += 1

        repo_full_name = repo["full_name"]
        cached_repo_state = state.get("repos", {}).get(repo_full_name, {})
        cached_branches = cached_repo_state.get("branches", {})

        branch_tips = get_repo_branch_tips(repo_full_name)
        if branch_tips is None:
            run_stats["repos_branch_tip_failures"] += 1
            if cached_repo_state:
                next_repos_state[repo_full_name] = cached_repo_state
                run_stats["repos_reused_cached_on_tip_failure"] += 1
            continue

        if include_all_branches:
            target_branch_tips = branch_tips
        else:
            default_branch = repo.get("default_branch")
            if default_branch and default_branch in branch_tips:
                target_branch_tips = {default_branch: branch_tips[default_branch]}
            else:
                target_branch_tips = {}

        next_branch_state = {}
        for branch_name, branch_tip_sha in target_branch_tips.items():
            run_stats["branches_seen"] += 1
            cached_branch_state = cached_branches.get(branch_name, {})
            cached_tip_sha = cached_branch_state.get("tip_sha")
            cached_shas = set(cached_branch_state.get("commit_shas", []))

            # Default to cached values when branch tip has not changed.
            branch_shas = cached_shas
            branch_tip_to_store = branch_tip_sha

            if not cached_tip_sha or cached_tip_sha != branch_tip_sha:
                branch_shas = None

                if cached_tip_sha:
                    run_stats["branch_compare_attempts"] += 1
                    compare_data = get_compare_data(
                        repo_full_name,
                        cached_tip_sha,
                        branch_tip_sha,
                    )
                    if compare_data is not None:
                        compare_status = compare_data.get("status")
                        commits = compare_data.get("commits", [])
                        total_commits = compare_data.get("total_commits", 0)
                        compare_is_truncated = total_commits > len(commits)

                        if (
                            compare_status in {"ahead", "identical"}
                            and not compare_is_truncated
                        ):
                            branch_shas = set(cached_shas)
                            added_from_delta = 0
                            for commit in commits:
                                sha = record_commit_metadata(commit, commit_metadata)
                                if sha:
                                    if sha not in branch_shas:
                                        added_from_delta += 1
                                    branch_shas.add(sha)
                            run_stats["branch_compare_delta_applied"] += 1
                            run_stats["delta_commits_added"] += added_from_delta
                        else:
                            run_stats["branch_compare_resync_required"] += 1
                    else:
                        run_stats["branch_compare_resync_required"] += 1

                if branch_shas is None:
                    run_stats["branch_full_resync_attempts"] += 1
                    full_scan_shas = get_branch_commits_full(
                        repo_full_name,
                        branch_name,
                        commit_metadata,
                    )
                    if full_scan_shas is None:
                        if cached_branch_state:
                            branch_shas = set(cached_shas)
                            branch_tip_to_store = cached_tip_sha
                            run_stats["branch_full_resync_fallback_cached"] += 1
                        else:
                            branch_shas = set()
                            run_stats["branch_full_resync_empty"] += 1
                    else:
                        branch_shas = full_scan_shas
                        run_stats["branch_full_resync_success"] += 1
            else:
                run_stats["branch_cache_hits"] += 1

            next_branch_state[branch_name] = {
                "tip_sha": branch_tip_to_store,
                "commit_shas": sorted(branch_shas),
            }

        next_repos_state[repo_full_name] = {
            "archived": repo.get("archived", False),
            "fork": repo.get("fork", False),
            "branches": next_branch_state,
        }

    active_commit_shas = set()
    for repo_state in next_repos_state.values():
        for branch_state in repo_state.get("branches", {}).values():
            active_commit_shas.update(branch_state.get("commit_shas", []))

    # Keep metadata only for commits currently reachable by counted branches.
    commit_metadata = {
        sha: metadata
        for sha, metadata in commit_metadata.items()
        if sha in active_commit_shas
    }

    user_commits = aggregate_user_counts(active_commit_shas, commit_metadata, members)

    if use_cache:
        state["repos"] = next_repos_state
        state["commit_metadata"] = commit_metadata
        save_state(state)

    if log_run_summary:
        logger.info(
            "per_user_commits summary: repos=%s processed=%s "
            "skipped_archived=%s skipped_forks=%s tip_failures=%s tip_failures_with_cache=%s "
            "branches=%s cache_hits=%s compare_attempts=%s compare_deltas=%s compare_resyncs=%s "
            "full_resync_attempts=%s full_resync_success=%s full_resync_cached=%s full_resync_empty=%s "
            "delta_commits_added=%s active_unique_shas=%s",
            run_stats["repos_total"],
            run_stats["repos_processed"],
            run_stats["repos_skipped_archived"],
            run_stats["repos_skipped_forks"],
            run_stats["repos_branch_tip_failures"],
            run_stats["repos_reused_cached_on_tip_failure"],
            run_stats["branches_seen"],
            run_stats["branch_cache_hits"],
            run_stats["branch_compare_attempts"],
            run_stats["branch_compare_delta_applied"],
            run_stats["branch_compare_resync_required"],
            run_stats["branch_full_resync_attempts"],
            run_stats["branch_full_resync_success"],
            run_stats["branch_full_resync_fallback_cached"],
            run_stats["branch_full_resync_empty"],
            run_stats["delta_commits_added"],
            len(active_commit_shas),
        )

    # Convert to a DataFrame
    data = []
    for user, counts in user_commits.items():
        data.append(
            [
                user,
                counts["total"],
                counts["last_month"],
                counts["last_6_months"],
            ]
        )

    df = pd.DataFrame(
        data,
        columns=[
            "User",
            "Total Commits",
            "Commits in Last Month",
            "Commits in Last 6 Months",
        ],
    )
    df = df[df["User"] != "unknown"]  # Remove 'unknown' users
    df["User"] = df["User"].apply(lambda user: f"[{user}](https://github.com/{user})")
    df = df.sort_values(by="Total Commits", ascending=False).head(10)  # Top 10 users

    # Create a Markdown table
    markdown_table = df.to_markdown(
        index=False,
        headers=[
            "User",
            "Total Commits",
            "Commits in Last Month",
            "Commits in Last 6 Months",
        ],
    )
    return markdown_table


def main():
    print(
        get_per_user_commits(
            include_all_branches=True,
            include_archived=True,
            include_forks=True,
            use_cache=True,
        )
    )


if __name__ == "__main__":
    main()
