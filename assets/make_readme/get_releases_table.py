import requests
import os
import pandas as pd
from datetime import datetime

# Replace these with your GitHub token and organization name
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
ORG_NAME = 'CCBR'

headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': f'token {GITHUB_TOKEN}'
}

def get_repos(org_name):
    repos = []
    page = 1
    while True:
        response = requests.get(f'https://api.github.com/orgs/{org_name}/repos?per_page=100&page={page}', headers=headers)
        if response.status_code != 200:
            break
        repos.extend(response.json())
        if len(response.json()) < 100:
            break
        page += 1
    return repos

def format_date(date_str):
    try:
        # Parse the date string and format it as YYYY-MM-DD
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return 'Unknown date'
    
def get_latest_release(repo_full_name):
    response = requests.get(f'https://api.github.com/repos/{repo_full_name}/releases/latest', headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def main():
    repos = get_repos(ORG_NAME)
    releases = []

    for repo in repos:
        latest_release = get_latest_release(repo['full_name'])
        if latest_release:
            repo_name = repo['name']
            release_name = latest_release['name']
            release_url = latest_release['html_url']
            release_date = latest_release['published_at']
            formatted_date = format_date(release_date)
            releases.append({
                'Repo Name': f"[{repo_name}](https://github.com/{ORG_NAME}/{repo_name})",
                'Release Name': f"[{release_name}]({release_url})",
                'Release Date': formatted_date
            })

    # Sort releases by date in descending order
    sorted_releases = sorted(releases, key=lambda x: x['Release Date'], reverse=True)

    # Create a DataFrame for Markdown table
    df = pd.DataFrame(sorted_releases)
    markdown_table = df.to_markdown(index=False, headers=['Repo Name', 'Release Name', 'Release Date'])

    # Print Markdown table
    print(markdown_table)

if __name__ == "__main__":
    main()
