import os
import sys
import requests
from datetime import datetime, timedelta

# Example usage:
# org_name = "CCBR"
# Load the GitHub token from the environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable not set")
# Inactivity threshold in days
DORMANT_THRESHOLD = 90

# GitHub API base URL
BASE_URL = "https://api.github.com"

# Headers for authentication
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

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

def get_user_activity(user):
    """Get the last public activity of a user."""
    url = f"{BASE_URL}/users/{user}/events"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    events = response.json()
    if events:
        return max(event["created_at"] for event in events)
    return None

def get_user_activity_in_org(user, org):
    """Get the last public activity of a user within a specific organization."""
    # URL to fetch user events
    url = f"{BASE_URL}/users/{user}/events"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    events = response.json()

    if not events:
        return None

    # Filter events for the specified organization
    org_events = [
        event for event in events
        if "repo" in event and event["repo"]["name"].startswith(f"{org}/")
    ]

    if org_events:
        #print(user)
        #for event in org_events:
        #    print(event["type"],event["created_at"])
        #sys.exit()
        # Return the latest activity in the organization
        return max(event["created_at"] for event in org_events)

    return None

def find_dormant_users(org, members):
    """Find dormant users based on the activity threshold."""
    dormant_users = []
    threshold_date = datetime.utcnow() - timedelta(days=DORMANT_THRESHOLD)

    for member in members:
        username = member["login"]
        #print(f"Checking activity for {username}...")
        last_activity = get_user_activity_in_org(username,org_name)
        if last_activity:
            last_active_date = datetime.strptime(last_activity, "%Y-%m-%dT%H:%M:%SZ")
            days_difference = (last_active_date - threshold_date).days
            #print(username)
            #print(last_active_date)
            #print(threshold_date)
            #print(days_difference)
            #sys.exit()
            if last_active_date < threshold_date:
                dormant_users.append({"username": username, "last_active": last_activity, "days_since_activity": days_difference})
        else:
            dormant_users.append({"username": username, "last_active": "No activity found", "days_since_activity": -1})
    return dormant_users

def get_days_since_last_activity(org_name, members, member_type="member"):
    """Get days since the last activity for all users in the organization."""
    users_activity = []
    current_date = datetime.utcnow()

    for member in members:
        username = member["login"]
        #print(f"Checking activity for {username}...")
        last_activity = get_user_activity_in_org(username, org_name)
        if last_activity:
            # Parse the last activity date
            last_active_date = datetime.strptime(last_activity, "%Y-%m-%dT%H:%M:%SZ")
            # Calculate days since last activity
            days_difference = (current_date - last_active_date).days
            users_activity.append({
                "username": username,
                "usertype": member_type,
                "last_active": last_activity,
                "days_since_activity": days_difference,
            })
        else:
            # No activity found
            users_activity.append({
                "username": username,
                "usertype": member_type,
                "last_active": "No activity found",
                "days_since_activity": -1,
            })

    return users_activity

def get_github_user_email(username):
    """
    Get the email address of a GitHub user if publicly available.
    :param username: GitHub username
    :return: Email address or a message indicating it is not public
    """
    # URL for the user's public profile
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 404:
        return f"User '{username}' not found."

    response.raise_for_status()
    user_data = response.json()

    # Check for email in the profile
    if user_data.get("email"):
        return user_data["email"]
    else:
        return f"Email for user '{username}' is not publicly available."

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

def get_activity_per_member(org_name, outdir):
    members = get_org_members(org_name)
    collaborators = get_outside_collaborators(org_name)
    outpath = os.path.join(outdir, org_name ,"README.md")

    # Extract the directory part of the path
    dir_name = os.path.dirname(outpath)
    
    # Create all necessary directories
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)

    #print("\nMember activity...")
    user_activity = get_days_since_last_activity(org_name, members, "member")
    user_activity.extend(get_days_since_last_activity(org_name, collaborators, "outside_collaborator"))
    
    with open(outpath, "w") as file:
        # Output the data as a Markdown table
        file.write("\n -1=No activity found!\n\n| github_handle   | member/collaborator | days_inactive |\n")
        file.write("|-----------------|----------------------|---------------|\n")

        for user in user_activity:
            # Extract user information
            username = user["username"]
            usertype = user["usertype"]
            days_since_activity = user["days_since_activity"]

            # Print the row in Markdown table format
            file.write(f"| {username:<15} | {usertype:<20} | {days_since_activity:<13} |\n")
    return outpath

def main():
    admin_organizations = get_admin_orgs(GITHUB_TOKEN)
    for org in admin_organizations:
        outpath = get_activity_per_member(org, "activity_data")
        print(f"  - [{org}]({outpath})")

if __name__ == "__main__":
    main()