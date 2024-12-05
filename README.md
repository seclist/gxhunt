# **GXHub** 🛠️

![GXHub GIF](gxhub.gif)

## **Overview**
**GXHub** is a command-line tool designed to gather and display detailed GitHub user information, including user profile data, event details, repository stats, and email addresses from commits. It leverages the GitHub API to extract valuable OSINT information from public GitHub profiles, and presents the data in a user-friendly table format with a grayscale color palette.

## **Features** ✨

- **User Profile Information**: Retrieves and displays GitHub user account details, including login, ID, avatar, and creation dates.
- **Email Extraction**: Finds email addresses hidden within `PushEvent` events from the user's recent activity.
- **Repositories**: Lists public repositories of the user, displaying important details such as repository name, description, language, stars, and last update.
- **Rich Table Display**: Outputs the gathered data in a visually appealing, tabular format using the `rich` library for enhanced readability.
- **Text File Output**: Saves all retrieved data into a text file named after the queried GitHub username.
- **Grayscale Color Palette**: Uses a subtle grayscale color palette for displaying information in the terminal.

## **Use Cases** 📖

- User profile analysis for outreach and research.
- Reverse email search through GitHub commit history.
- Inspect public repositories and activities for contribution tracking.
- Monitor two-factor authentication (2FA) status and account security.
- Collect data for cybersecurity, OSINT, and research purposes.

## **Prerequisites** 🛠️

To run this tool, you'll need:

- Python 3.x
- The `requests` library
- The `rich` library for improved table output

You can install the required libraries using `pip`:

```sh
pip install requests rich
```

## **Installation** ⚙️

1. Clone the repository or download the script as `gxhub.py`.
2. Install dependencies by running the following command:

    ```sh
    pip install -r requirements.txt
    ```

## **Usage** 🚀

1. Save the script to a file, e.g., `gxhub.py`.
2. Execute the script from the command line, passing the GitHub username as an argument:

    ```sh
    python gxhub.py <github_username>
    ```

   Replace `<github_username>` with the actual GitHub username you want to query.

## **Output** 📊

The tool will display the following information on the console:

- **GitHub User Info**:
    - `Login`, `ID`, `Node ID`, `Avatar URL`, `Profile URL`, `Type`, `Admin`, `Created`, `Last Updated`, and **2FA Status**.
    - **User Info**: `Name`, `Company`, `Location`, `Email`, `Bio`, and `Twitter`.
  
- **Email Addresses Found**: A list of email addresses found in commits, if available.

- **Public Repositories**: Lists the user’s public repositories, showing:
    - `Name`, `Description`, `Language`, `Stars`, and `Last Updated`.

The same data will be saved in a `.txt` file named `<github_username>.txt`.

### **Example Output:**
```
GitHub User Info:
Login: johndoe
ID: 123456
Node ID: MDQ6VXNlcjEyMzQ1Ng==
Avatar URL: https://avatars.githubusercontent.com/u/123456?v=4
Profile URL: https://github.com/johndoe
Type: user
Admin: False
Created: 2020-05-01T00:00:00Z
Last Updated: 2024-01-01T00:00:00Z
Two Factor Authentication: False

User Info:
Name: John Doe
Company: Example Inc.
Location: New York, USA
Email: johndoe@example.com
Bio: Software Developer
Twitter: johndoe

Email Addresses Found:
johndoe@example.com

Public Repositories:
Repository Name: project1
Description: A sample project.
Language: Python
Stars: 25
Last Updated: 2024-01-01T00:00:00Z
```

## **Saving to File** 📂

All the fetched data is saved to a text file with the name `<github_username>.txt`. The file will contain the same structured information seen in the console output.

## **Future Features** 🔮

Here are some planned future features for GXHub:

- **GitHub Issues and Pull Requests**: Retrieve and display open issues and pull requests from a user's repositories.
- **Repository Forks and Contributions**: Track the number of forks and contributions a user has made to other repositories.
- **Security Alerts**: Fetch and display any security vulnerabilities associated with the user's repositories.
- **Commit History Analysis**: Provide insights into the user's commit history, including the number of commits over time, frequency, and more.
- **Collaborators and Teams**: Retrieve and display information about collaborators and teams the user is part of.
- **API Rate Limit Handling**: Implement automatic handling of GitHub API rate limits to prevent disruptions during extended queries.

## **Notes** ℹ️

- **Two-factor Authentication (2FA)**: GitHub's API does not allow you to check the 2FA status of other users. The check will only return accurate results for the authenticated user (if an OAuth token is provided).
- **API Rate Limiting**: Be aware of GitHub's API rate limits. If you exceed the limits, you'll need to wait before making additional requests.
- **Public Data Only**: This tool only fetches publicly available information from GitHub profiles and events.

## **License** 📜

This tool is provided "as-is". Use it responsibly and ensure compliance with GitHub’s API usage terms. Always respect privacy and do not use this tool for unethical activities.


