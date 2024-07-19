import requests
import os
import pandas as pd
from collections import defaultdict
from datetime import datetime, timedelta

# Replace these with your GitHub token and organization name
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
ORG_NAME = 'CCBR'
# ORG_NAME = 'CCRGeneticsBranch'
# ORG_NAME = 'NIDAP-Community'
# ORG_NAME = 'NCI-VB'

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

def get_members(org_name):
    members = set()
    page = 1
    while True:
        response = requests.get(f'https://api.github.com/orgs/{org_name}/members?per_page=100&page={page}', headers=headers)
        if response.status_code != 200:
            break
        page_members = response.json()
        if not page_members:
            break
        for member in page_members:
            members.add(member['login'])
        page += 1
    return members

def get_outside_collaborators(repo_full_name):
    collaborators = set()
    page = 1
    while True:
        response = requests.get(f'https://api.github.com/repos/{repo_full_name}/collaborators?affiliation=outside&per_page=100&page={page}', headers=headers)
        if response.status_code != 200:
            break
        outside_collaborators = response.json()
        if not outside_collaborators:
            break
        for collaborator in outside_collaborators:
            collaborators.add(collaborator['login'])
        page += 1
    return collaborators

def get_commits_count(repo_full_name, members_and_collaborators):
    commits_count_by_user = defaultdict(lambda: {'total': 0, 'last_month': 0, 'last_6_months': 0})
    page = 1
    today = datetime.utcnow()
    one_month_ago = today - timedelta(days=30)
    six_months_ago = today - timedelta(days=180)
    
    while True:
        response = requests.get(f'https://api.github.com/repos/{repo_full_name}/commits?per_page=100&page={page}', headers=headers)
        if response.status_code != 200:
            break
        commits = response.json()
        if not commits:
            break
        
        for commit in commits:
            author_login = commit['author']['login'] if commit['author'] else 'unknown'
            commit_date_str = commit['commit']['author']['date']
            commit_date = datetime.strptime(commit_date_str, '%Y-%m-%dT%H:%M:%SZ')
            
            if author_login != 'unknown' and author_login in members_and_collaborators:
                commits_count_by_user[author_login]['total'] += 1
                if commit_date >= one_month_ago:
                    commits_count_by_user[author_login]['last_month'] += 1
                if commit_date >= six_months_ago:
                    commits_count_by_user[author_login]['last_6_months'] += 1
        
        page += 1
    
    return commits_count_by_user

def main():
    members = get_members(ORG_NAME)
    repos = get_repos(ORG_NAME)
    
    # Collect outside collaborators
    outside_collaborators = set()
    for repo in repos:
        repo_full_name = repo['full_name']
        # print(f"Fetching outside collaborators for repository: {repo_full_name}")
        outside_collaborators.update(get_outside_collaborators(repo_full_name))
    
    members_and_collaborators = members.union(outside_collaborators)
    
    user_commits = defaultdict(lambda: {'total': 0, 'last_month': 0, 'last_6_months': 0})

    for repo in repos:
        repo_full_name = repo['full_name']
        # print(f"Processing repository: {repo_full_name}")
        commits_count_by_user = get_commits_count(repo_full_name, members_and_collaborators)
        for user, counts in commits_count_by_user.items():
            user_commits[user]['total'] += counts['total']
            user_commits[user]['last_month'] += counts['last_month']
            user_commits[user]['last_6_months'] += counts['last_6_months']

    # Convert to a DataFrame
    data = []
    for user, counts in user_commits.items():
        data.append([
            user,
            counts['total'],
            counts['last_month'],
            counts['last_6_months']
        ])
    
    df = pd.DataFrame(data, columns=['User', 'Total Commits', 'Commits in Last Month', 'Commits in Last 6 Months'])
    df = df[df['User'] != 'unknown']  # Remove 'unknown' users
    df = df.sort_values(by='Total Commits', ascending=False).head(10)  # Top 10 users

    # Create a Markdown table
    markdown_table = df.to_markdown(index=False, headers=['User', 'Total Commits', 'Commits in Last Month', 'Commits in Last 6 Months'])
    print(markdown_table)

if __name__ == "__main__":
    main()
