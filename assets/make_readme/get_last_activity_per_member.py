import requests,sys,os
from datetime import datetime
VERBOSE=0 # 0 means no comments ... anything else means print progress comments

# This script retrieves and reports the last activity of members and outside collaborators 
# for GitHub organizations where the authenticated user has an admin role. 
# It fetches the list of organizations, members, outside collaborators, and repository events 
# to determine the last activity date for each user. The results are written to a markdown file 
# for each organization, detailing the days since the last activity for each member and collaborator.

BASE_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}
def get_admin_orgs(github_token):
    """
    Retrieves the list of organizations where the authenticated user has an admin role.
    
    Args:
        github_token (str): A GitHub personal access token.
    
    Returns:
        list: A list of organization logins where the user is an admin.
    """
    url = "https://api.github.com/user/memberships/orgs"
    headers = {
        "Authorization": f"token {github_token}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        memberships = response.json()
        admin_orgs = [
            org['organization']['login']
            for org in memberships
            if org.get('role') == 'admin'
        ]
        return admin_orgs
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
    
def get_org_members(org):
    """Get all members of the organization."""
    url = f"{BASE_URL}/orgs/{org}/members"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_outside_collaborators(org):
    """Get all outside collaborators of the organization."""
    url = f"{BASE_URL}/orgs/{org}/outside_collaborators"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_all_repos(org):
    """Get all repos in the org"""
    repos = []
    page = 1
    while True:
        url = f"{BASE_URL}/orgs/{org}/repos"
        params = {"type": "all", "per_page": 100, "page": page}
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        page_repos = response.json()
        if not page_repos:
            break
        repos.extend(page_repos)
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

    try:
        while True:
            response = requests.get(f"{url}?per_page=100&page={page}", headers=HEADERS)
            response.raise_for_status()
            page_events = response.json()

            if not page_events:
                break

            events.extend(page_events)
            page += 1
            if page == 4: break # get only top 300

        return events

    except requests.exceptions.RequestException as e:
        # print(f"Error fetching events for repo '{repo}': {e}")
        return []

def report_org_activity(org,outmd):
    """Write org activity to a markdown file"""
    # Example Usage
    # org = sys.argv[1]
    # outmd = sys.argv[2]

    # Extract the directory part of the path
    dir_name = os.path.dirname(outmd)
    
    # Create all necessary directories
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    try:
        if VERBOSE !=0: print(f"Organization: {org}")
        repositories = get_all_repos(org)
        if VERBOSE !=0: print(f"Total repositories: {len(repositories)}")
        members = get_org_members(org)
        if VERBOSE !=0: print(f"Total members: {len(members)}")
        collaborators = get_outside_collaborators(org)
        if VERBOSE !=0: print(f"Total collaborators: {len(collaborators)}")
        # events=list_repo_events(org,sys.argv[1])
        # print(len(events))
        last_events=dict()
        for repo in repositories:
            reponame=repo["name"]
            events=list_repo_events(org,reponame)
            users=set()
            for event in events:
                user=event['actor']['login']
                users.add(user)
                if not user in last_events:
                    last_events[user]=[]
                last_events[user].append(event['created_at'])
            for user in users:
                last_events[user]=[max(last_events[user])]
            if VERBOSE !=0: print(f"\tFinished working with repo: {org}/{reponame}; Found {len(users)} users and {len(events)} events.")

        with open(outmd, "w") as file:
            file.write("\n| github_handle   | member/collaborator | days_inactive |\n")
            file.write("|-----------------|----------------------|---------------|\n")
            days_inactivity=dict()
            for member in members:
                username = member["login"]
                if not username in last_events:
                    days_inactivity[username]="No Activity Found"
                else:
                    last_event = max(last_events[username])
                    event_date = datetime.fromisoformat(last_event).date()
                    today_date = datetime.now().date()
                    days_inactivity[username]=str((today_date - event_date).days)
                # print(username,"member",days_inactivity[username])
                days_since_activity=days_inactivity[username]
                usertype="member"
                username_with_hyperlink = f"[{username}](https://github.com/{username})"
                file.write(f"| {username_with_hyperlink:<15} | {usertype:<20} | {days_since_activity:<13} |\n")

            for collaborator in collaborators:
                username = collaborator["login"]
                if not username in last_events:
                    days_inactivity[username]="No Activity Found"
                else:
                    last_event = max(last_events[user])
                    event_date = datetime.fromisoformat(last_event).date()
                    today_date = datetime.now().date()
                    days_inactivity[username]=str((today_date - event_date).days)
                # print(username,"outside_collaborator",days_inactivity[username])
                days_since_activity=days_inactivity[username]
                usertype="collaborator"
                username_with_hyperlink = f"[{username}](https://github.com/{username})"
                file.write(f"| {username_with_hyperlink:<15} | {usertype:<20} | {days_since_activity:<13} |\n")
    except:
        return False
    return True


def main():
    organizations = get_admin_orgs(GITHUB_TOKEN)
    print(f"\n")
    # organizations = ["NCI-CCDI"]
    # organizations = ["abcswebapps"]
    for org in organizations:
        outpath = os.path.join("activity_data",org,"README.md")
        if report_org_activity(org, outpath):
            print(f"  - [{org}]({outpath})")

if __name__ == "__main__":
    main()