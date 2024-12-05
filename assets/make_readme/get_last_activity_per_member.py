import os
import sys
import requests
from datetime import datetime, timedelta

# Example usage:
ORG_NAME = "CCBR"
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
        last_activity = get_user_activity_in_org(username,ORG_NAME)
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

def get_days_since_last_activity(org, members, member_type="member"):
    """Get days since the last activity for all users in the organization."""
    users_activity = []
    current_date = datetime.utcnow()

    for member in members:
        username = member["login"]
        #print(f"Checking activity for {username}...")
        last_activity = get_user_activity_in_org(username, ORG_NAME)
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


def main():
    #print("Fetching organization members...")
    members = get_org_members(ORG_NAME)
    #print(members)
    #print(len(members))

    #print("Fetching outside collaborators...")
    collaborators = get_outside_collaborators(ORG_NAME)
    #print(collaborators)
    #print(len(collaborators))

    #print("Finding dormant members...")
    #dormant_members = find_dormant_users(ORG_NAME, members)
    #print("\nDormant Members:")
    #for user in dormant_members:
    #    print(user)

    #print("\nFinding dormant collaborators...")
    #dormant_collaborators = find_dormant_users(ORG_NAME, collaborators)
    #print("\nDormant Outside Collaborators:")
    #for user in dormant_collaborators:
    #    print(user)

    #print("\nMember activity...")
    user_activity = get_days_since_last_activity(ORG_NAME, members, "member")
    user_activity.extend(get_days_since_last_activity(ORG_NAME, collaborators, "outside_collaborator"))
    # Output the data as a Markdown table
    print("| github_handle   | member/collaborator | days_inactive |")
    print("|-----------------|----------------------|---------------|")

    for user in user_activity:
        # Extract user information
        username = user["username"]
        usertype = user["usertype"]
        days_since_activity = user["days_since_activity"]

        # Print the row in Markdown table format
        print(f"| {username:<15} | {usertype:<20} | {days_since_activity:<13} |")

if __name__ == "__main__":
    main()