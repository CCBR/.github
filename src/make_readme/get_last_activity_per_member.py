import requests
import os
import logging
from datetime import datetime

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

VERBOSE = 0  # 0 means no comments ... anything else means print progress comments

# This script retrieves and reports the last activity of members and outside collaborators
# for GitHub organizations where the authenticated user has an admin role.
# It fetches the list of organizations, members, outside collaborators, and repository events
# to determine the last activity date for each user. The results are written to a markdown file
# for each organization, detailing the days since the last activity for each member and collaborator.

BASE_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable not set")
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

logger = logging.getLogger(__name__)


def get_admin_orgs(github_token):
    """
    Retrieves the list of organizations where the authenticated user has an admin role.

    Args:
        github_token (str): A GitHub personal access token.

    Returns:
        list: A list of organization logins where the user is an admin.
    """
    url = "https://api.github.com/user/memberships/orgs"
    headers = {"Authorization": f"token {github_token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise_api_error(response, "organization memberships")

    memberships = response.json()
    admin_orgs = [
        org["organization"]["login"]
        for org in memberships
        if org.get("role") == "admin"
    ]
    return admin_orgs


def get_org_members(org):
    """Get all members of the organization, handling pagination."""
    members = []
    page = 1
    while True:
        url = f"{BASE_URL}/orgs/{org}/members"
        response = requests.get(url, headers=HEADERS, params={"per_page": 100, "page": page})
        if response.status_code != 200:
            raise_api_error(response, f"members for org '{org}'")
        page_members = response.json()
        if not page_members:
            break
        members.extend(page_members)
        page += 1
    return members


def get_outside_collaborators(org):
    """Get all outside collaborators of the organization, handling pagination."""
    collaborators = []
    page = 1
    while True:
        url = f"{BASE_URL}/orgs/{org}/outside_collaborators"
        response = requests.get(url, headers=HEADERS, params={"per_page": 100, "page": page})
        if response.status_code != 200:
            raise_api_error(response, f"outside collaborators for org '{org}'")
        page_collabs = response.json()
        if not page_collabs:
            break
        collaborators.extend(page_collabs)
        page += 1
    return collaborators


def get_all_repos(org):
    """Get all repos in the org"""
    repos = []
    page = 1
    has_more_pages = True
    while has_more_pages:
        url = f"{BASE_URL}/orgs/{org}/repos"
        params = {"type": "all", "per_page": 100, "page": page}
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code != 200:
            raise_api_error(response, f"repositories for org '{org}'")
        page_repos = response.json()
        has_more_pages = bool(page_repos)
        repos.extend(page_repos)
        if has_more_pages:
            page += 1
    return repos


def list_repo_events(org, repo):
    """
    List all public events for a given repository in an organization.

    Args:
        org (str): The GitHub organization name.
        repo (str): The repository name.

    Returns:
        list: A list of events, or an empty list if no events are found.
    """
    url = f"{BASE_URL}/repos/{org}/{repo}/events"
    events = []
    page = 1

    has_more_pages = True
    while has_more_pages and page <= 3:
        response = requests.get(f"{url}?per_page=100&page={page}", headers=HEADERS)
        if response.status_code != 200:
            if is_critical_api_error(response):
                raise_api_error(response, f"events for repo '{org}/{repo}'")
            log_noncritical_api_error(
                response,
                f"events for repo '{org}/{repo}'",
                "an empty event list",
                logger,
            )
            has_more_pages = False
            continue
        page_events = response.json()
        has_more_pages = bool(page_events)
        events.extend(page_events)
        if has_more_pages:
            page += 1

    return events


def report_org_activity(org, outmd):
    """Write org activity to a markdown file"""
    # Example Usage
    # org = sys.argv[1]
    # outmd = sys.argv[2]

    # Extract the directory part of the path
    dir_name = os.path.dirname(outmd)

    # Create all necessary directories
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    if VERBOSE != 0:
        print(f"Organization: {org}")
    repositories = get_all_repos(org)
    if not repositories:
        raise RuntimeError(
            f"No repositories were returned for org '{org}'. "
            "Critical README data is unavailable. "
            "Check whether GITHUB_TOKEN is expired or missing required permissions."
        )
    if VERBOSE != 0:
        print(f"Total repositories: {len(repositories)}")
    members = get_org_members(org)
    if not members:
        raise RuntimeError(
            f"No members were returned for org '{org}'. "
            "Critical README data is unavailable. "
            "Check whether GITHUB_TOKEN is expired or missing required permissions."
        )
    if VERBOSE != 0:
        print(f"Total members: {len(members)}")
    collaborators = get_outside_collaborators(org)
    if VERBOSE != 0:
        print(f"Total collaborators: {len(collaborators)}")
    # events=list_repo_events(org,sys.argv[1])
    # print(len(events))
    last_events = dict()
    for repo in repositories:
        reponame = repo["name"]
        events = list_repo_events(org, reponame)
        users = set()
        for event in events:
            user = event["actor"]["login"]
            users.add(user)
            if user not in last_events:
                last_events[user] = []
            last_events[user].append(event["created_at"])
        for user in users:
            last_events[user] = [max(last_events[user])]
        if VERBOSE != 0:
            print(
                f"\tFinished working with repo: {org}/{reponame}; Found {len(users)} users and {len(events)} events."
            )

    with open(outmd, "w") as file:
        file.write("\n| github_handle   | member/collaborator | days_inactive |\n")
        file.write("|-----------------|----------------------|---------------|\n")
        days_inactivity = dict()
        for member in members:
            username = member["login"]
            if username not in last_events:
                days_inactivity[username] = "No Activity Found"
            else:
                last_event = max(last_events[username])
                event_date = datetime.fromisoformat(last_event.replace("Z", "+00:00")).date()
                today_date = datetime.now().date()
                days_inactivity[username] = str((today_date - event_date).days)
            # print(username,"member",days_inactivity[username])
            days_since_activity = days_inactivity[username]
            usertype = "member"
            username_with_hyperlink = f"[{username}](https://github.com/{username})"
            file.write(
                f"| {username_with_hyperlink:<15} | {usertype:<20} | {days_since_activity:<13} |\n"
            )

        for collaborator in collaborators:
            username = collaborator["login"]
            if username not in last_events:
                days_inactivity[username] = "No Activity Found"
            else:
                last_event = max(last_events[username])
                event_date = datetime.fromisoformat(last_event.replace("Z", "+00:00")).date()
                today_date = datetime.now().date()
                days_inactivity[username] = str((today_date - event_date).days)
            # print(username,"outside_collaborator",days_inactivity[username])
            days_since_activity = days_inactivity[username]
            usertype = "collaborator"
            username_with_hyperlink = f"[{username}](https://github.com/{username})"
            file.write(
                f"| {username_with_hyperlink:<15} | {usertype:<20} | {days_since_activity:<13} |\n"
            )
    return True


def get_last_activity_per_member():
    organizations = get_admin_orgs(GITHUB_TOKEN)
    if not organizations:
        raise RuntimeError(
            "No admin organizations were returned from GitHub API. "
            "Critical README data is unavailable. "
            "Check whether GITHUB_TOKEN is expired or missing required permissions."
        )
    lines = []
    # organizations = ["NCI-CCDI"]
    # organizations = ["abcswebapps"]
    for org in organizations:
        outpath = os.path.join("activity_data", org, "README.md")
        if report_org_activity(org, outpath):
            lines.append(f"- [{org}]({outpath})")
    return "\n".join(lines)


def main():
    output = get_last_activity_per_member()
    if output:
        print(output)


if __name__ == "__main__":
    main()
