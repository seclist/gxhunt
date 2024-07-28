import requests
import sys
import textwrap

def print_banner():
    banner = """
 ██████  ██   ██ ██   ██ ██    ██ ██████  
██        ██ ██  ██   ██ ██    ██ ██   ██ 
██   ███   ███   ███████ ██    ██ ██████  
██    ██  ██ ██  ██   ██ ██    ██ ██   ██ 
 ██████  ██   ██ ██   ██  ██████  ██████  
    """
    print(textwrap.dedent(banner))

def get_user_info(username):
    try:
        user_api_url = f"https://api.github.com/users/{username}"
        response = requests.get(user_api_url)
        response.raise_for_status()
        user_data = response.json() 

        user_info = textwrap.dedent(f"""
        Account info
        login: {user_data.get('login', 'N/A')}
        id: {user_data.get('id', 'N/A')}
        node id: {user_data.get('node_id', 'N/A')}
        avatar: {user_data.get('avatar_url', 'N/A')}
        url: {user_data.get('html_url', 'N/A')}
        type: {user_data.get('type', 'N/A')}
        admin: {user_data.get('site_admin', 'N/A')}
        created: {user_data.get('created_at', 'N/A')}
        last updated: {user_data.get('updated_at', 'N/A')}
        two factor: {user_data.get('two_factor_authentication', 'N/A')}

        User info
        Name: {user_data.get('name', 'N/A')}
        company: {user_data.get('company', 'N/A')}
        location: {user_data.get('location', 'N/A')}
        email: {user_data.get('email', 'N/A')}
        bio: {user_data.get('bio', 'N/A')}
        twitter: {user_data.get('twitter_username', 'N/A')}
        """)
        return user_info

    except Exception as e:
        return f"Error retrieving user info: {str(e)}"

def get_github_events(username):
    try:
        github_api_url = f"https://api.github.com/users/{username}/events/public"
        response = requests.get(github_api_url)
        response.raise_for_status()
        github_data = response.json()

        email_addresses = set()
        for event in github_data:
            if event['type'] == 'PushEvent':
                for commit in event['payload']['commits']:
                    email_addresses.add(commit['author']['email'])

        if email_addresses:
            email_info = "\nEmail addresses found in commits:\n" + "\n".join(f"{email}" for email in email_addresses)
        else:
            email_info = "\nNo email addresses found in commits."

        return email_info

    except Exception as e:
        return f"Error retrieving events: {str(e)}"

if __name__ == "__main__":
    print_banner()

    if len(sys.argv) != 2:
        print("Usage: python script.py <github_username>")
        sys.exit(1)

    username = sys.argv[1]

    user_info = get_user_info(username)
    event_info = get_github_events(username)

    output = user_info + "\n" + event_info

    print(output)

    with open(f"{username}.txt", "w") as file:
        file.write(output)
    
    print(f"\nThe information has been saved to {username}.txt")
