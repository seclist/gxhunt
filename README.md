# GXHub 🛠️

## Overview

**GXHub** is a command-line tool that extracts and displays GitHub user information as well as uncovering hidden email addresses from public events. This tool queries the GitHub API to gather user data and event details, and it outputs this information in a well-structured format.

## Features ✨

- Retrieves and displays GitHub user account information.
- Extracts email addresses from public `PushEvent` events.
- Checks and displays whether two-factor authentication (2FA) is enabled for authenticated users.
- Saves the fetched information to a text file named after the queried GitHub username.

## Uses 📖

- User Profile Verification
- Username to Email Address
- Two-Factor Authentication (2FA) Status Monitoring
- Profile Data Collection for Outreach

## Prerequisites 🛠️

- Python 3.x
- `requests` library

    You can install the `requests` library using pip:

    ```sh
    pip install requests
    ```

## Usage 🚀

1. Save the script to a file, for example `gxhub.py`.
2. Run the script from the command line, passing the GitHub username as an argument:

    ```sh
    python gxhub.py <github_username>
    ```

   Replace `<github_username>` with the actual GitHub username you want to query.

## Output 📊

The tool will print the following information to the console:

- **Account info**
  - `login`: The GitHub username.
  - `id`: The unique ID of the user.
  - `node id`: The node ID of the user.
  - `avatar`: URL to the user's avatar image.
  - `url`: URL to the user's GitHub profile.
  - `type`: Type of account (e.g., `user`).
  - `admin`: Whether the user is an admin.
  - `created`: Date and time the account was created.
  - `last updated`: Date and time the account was last updated.
  - `two factor`: Whether two-factor authentication is enabled.

- **User info**
  - `Name`: The user's full name.
  - `company`: The company the user is associated with.
  - `location`: The user's location.
  - `email`: The user's email address.
  - `bio`: The user's biography.
  - `twitter`: The user's Twitter handle.

- **Email addresses found in commits:**
  - List of hidden email addresses found in `PushEvent` events.

The same information is saved to a text file named `<github_username>.txt`.

## Notes ℹ️

- **Two-factor Authentication (2FA)**: Checking 2FA status for other users is not possible through GitHub's public API. The 2FA status check will only work for the authenticated user associated with the provided access token. Ensure your token has the necessary permissions for accurate results.
- **Future Updates**: This tool will be updated regulary with new OSINT techniques for github accounts

## License 📜

This tool is provided as-is. Use it at your own risk, and ensure compliance with GitHub's API usage policies.

