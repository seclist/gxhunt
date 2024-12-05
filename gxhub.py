import requests
import sys
import textwrap
from rich.table import Table
from rich.console import Console


def print_banner():
    banner = """
 ██████  ██   ██ ██   ██ ██    ██ ██████  
██        ██ ██  ██   ██ ██    ██ ██   ██ 
██   ███   ███   ███████ ██    ██ ██████  
██    ██  ██ ██  ██   ██ ██    ██ ██   ██ 
 ██████  ██   ██ ██   ██  ██████  ██████  
    """
    print(textwrap.dedent(banner))


def display_table(data, title):
    table = Table(title=title)
    table.add_column("Field", style="grey53", justify="right")
    table.add_column("Value", style="grey85", justify="left")
    for field, value in data.items():
        table.add_row(field, str(value) if value else "N/A")
    console = Console()
    console.print(table)


def get_user_info(username):
    try:
        user_api_url = f"https://api.github.com/users/{username}"
        response = requests.get(user_api_url, timeout=10)
        response.raise_for_status()
        user_data = response.json()
        user_info = {
            "Login": user_data.get("login"),
            "ID": user_data.get("id"),
            "Node ID": user_data.get("node_id"),
            "Avatar URL": user_data.get("avatar_url"),
            "URL": user_data.get("html_url"),
            "Type": user_data.get("type"),
            "Admin": user_data.get("site_admin"),
            "Created": user_data.get("created_at"),
            "Last Updated": user_data.get("updated_at"),
            "Name": user_data.get("name"),
            "Company": user_data.get("company"),
            "Location": user_data.get("location"),
            "Email": user_data.get("email"),
            "Bio": user_data.get("bio"),
            "Twitter": user_data.get("twitter_username"),
        }
        display_table(user_info, title="GitHub User Info")
        return user_info
    except Exception as e:
        print(f"Error retrieving user info: {str(e)}")
        return None


def get_github_events(username):
    try:
        github_api_url = f"https://api.github.com/users/{username}/events/public"
        response = requests.get(github_api_url, timeout=10)
        response.raise_for_status()
        github_data = response.json()
        email_addresses = set()
        for event in github_data:
            if event['type'] == 'PushEvent':
                for commit in event['payload']['commits']:
                    email_addresses.add(commit['author']['email'])
        if email_addresses:
            email_data = {f"Email {i+1}": email for i, email in enumerate(email_addresses)}
        else:
            email_data = {"Message": "No email addresses found in commits."}
        display_table(email_data, title="Email Addresses Found in Commits")
        return email_addresses
    except Exception as e:
        print(f"Error retrieving events: {str(e)}")
        return None

def get_user_repositories(username):
    try:
        api_url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        repos = response.json()
        repo_data = []
        for repo in repos:
            repo_data.append({
                "Name": repo.get("name", "N/A"),
                "Description": repo.get("description", "N/A") or "No description",
                "Language": repo.get("language", "N/A"),
                "Stars": repo.get("stargazers_count", 0),
                "Last Updated": repo.get("updated_at", "N/A"),
            })
        if repo_data:
            table = Table(title="User Repositories")
            table.add_column("Name", style="grey53")
            table.add_column("Description", style="grey85")
            table.add_column("Language", style="grey70")
            table.add_column("Stars", style="grey53", justify="right")
            table.add_column("Last Updated", style="grey85")
            for repo in repo_data:
                table.add_row(
                    repo["Name"],
                    repo["Description"],
                    repo["Language"],
                    str(repo["Stars"]),
                    repo["Last Updated"],
                )
            console = Console()
            console.print(table)
        return repo_data
    except Exception as e:
        print(f"Error retrieving repositories: {str(e)}")
        return []


if __name__ == "__main__":
    print_banner()
    if len(sys.argv) != 2:
        print("Usage: python gxhub.py <github_username>")
        sys.exit(1)
    username = sys.argv[1]
    user_info = get_user_info(username)
    email_info = get_github_events(username)
    repo_info = get_user_repositories(username)
    if user_info or email_info or repo_info:
        with open(f"{username}.txt", "w") as file:
            file.write("GitHub User Info:\n")
            if user_info:
                for key, value in user_info.items():
                    file.write(f"{key}: {value}\n")
            else:
                file.write("No user information found.\n")
            file.write("\nEmail Addresses Found:\n")
            if email_info:
                for email in email_info:
                    file.write(f"{email}\n")
            else:
                file.write("No email addresses found in commits.\n")
            file.write("\nPublic Repositories:\n")
            if repo_info:
                for repo in repo_info:
                    file.write(f"\nRepository Name: {repo['Name']}\n")
                    file.write(f"Description: {repo['Description']}\n")
                    file.write(f"Language: {repo['Language']}\n")
                    file.write(f"Stars: {repo['Stars']}\n")
                    file.write(f"Last Updated: {repo['Last Updated']}\n")
            else:
                file.write("No repositories found.\n")
        print(f"\nThe information has been saved to {username}.txt")
