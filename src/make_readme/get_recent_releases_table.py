import requests
import os
import argparse
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

exclude_list = ["nf-sandbox"]

# Replace these with your GitHub token and organization name
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable not set")
ORG_NAME = "CCBR"

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}",
}


def _raise_api_error(response, endpoint):
    raise RuntimeError(
        f"Failed to retrieve {endpoint} from GitHub API "
        f"(status {response.status_code}). "
        "Critical README data is unavailable. "
        "Check whether GITHUB_TOKEN is expired or missing required permissions."
    )


def get_date_n_months_ago(n_months):
    today = datetime.now()
    n_months_ago = today - relativedelta(months=n_months)
    return n_months_ago.strftime("%Y-%m-%d")


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
            _raise_api_error(response, f"repositories for org '{org_name}'")
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


def format_date(date_str):
    try:
        # Parse the date string and format it as YYYY-MM-DD
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        return "Unknown date"


def get_latest_release(repo_full_name):
    response = requests.get(
        f"https://api.github.com/repos/{repo_full_name}/releases/latest",
        headers=headers,
    )
    if response.status_code == 200:
        return response.json()
    if response.status_code in {401, 403}:
        _raise_api_error(response, f"latest release for repo '{repo_full_name}'")
    return None


def get_open_issues_count(repo_full_name):
    response = requests.get(
        f"https://api.github.com/repos/{repo_full_name}/issues?state=open",
        headers=headers,
    )
    if response.status_code == 200:
        return len(response.json())
    _raise_api_error(response, f"open issues for repo '{repo_full_name}'")


def get_recent_releases_table(nmonths=0):
    repos = get_repos(ORG_NAME)
    releases = []
    cutoff_date = get_date_n_months_ago(nmonths)

    for repo in repos:
        latest_release = get_latest_release(repo["full_name"])
        open_issues_count = get_open_issues_count(repo["full_name"])
        if latest_release:
            repo_name = repo["name"]
            if repo_name in exclude_list:
                continue
            # release_name = latest_release['name']
            release_url = latest_release["html_url"]
            release_name = release_url.split("/")[-1]
            release_date = latest_release["published_at"]
            formatted_date = format_date(release_date)
            if formatted_date != "Unknown date" and (
                nmonths == 0 or formatted_date >= cutoff_date
            ):
                releases.append(
                    {
                        "Repo Name": f"[{repo_name}](https://github.com/{ORG_NAME}/{repo_name})",
                        "Release Name": f"[{release_name}]({release_url})",
                        "Release Date": formatted_date,
                        "Open Issues": open_issues_count,
                    }
                )

    # Sort releases by date in descending order
    sorted_releases = sorted(releases, key=lambda x: x["Release Date"], reverse=True)

    # Create a DataFrame for Markdown table
    df = pd.DataFrame(sorted_releases)
    markdown_table = df.to_markdown(
        index=False,
        headers=["Repo Name", "Release Name", "Release Date", "Open Issues"],
    )

    return f"{markdown_table}\n"


def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub repository releases.")
    parser.add_argument(
        "--nmonths",
        type=int,
        default=0,
        help="Number of months to filter releases. If not provided, shows all releases.",
    )
    args = parser.parse_args()

    print(get_recent_releases_table(nmonths=args.nmonths), end="")


if __name__ == "__main__":
    main()
