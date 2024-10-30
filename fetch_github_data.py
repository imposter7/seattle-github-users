import requests
import pandas as pd
import os

# Replace with your GitHub access token
GITHUB_TOKEN = "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"

# GitHub API URLs
USER_URL = "https://api.github.com/search/users"
REPO_URL = "https://api.github.com/users/{}/repos"

# Set headers for authorization
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Function to get users from Seattle with over 200 followers
def get_users():
    users = []
    page = 1
    while True:
        params = {
            'q': 'location:Seattle followers:>200',
            'per_page': 100,
            'page': page
        }
        response = requests.get(USER_URL, headers=headers, params=params)
        data = response.json()

        # Check if 'items' is in the response
        if 'items' not in data or not data['items']:
            break

        for user in data['items']:
            users.append({
                'login': user['login'],
                'name': user.get('name', ''),
                'company': user.get('company', '').strip('@ ').upper(),
                'location': user.get('location', ''),
                'email': user.get('email', ''),
                'hireable': user.get('hireable', ''),
                'bio': user.get('bio', ''),
                'public_repos': user.get('public_repos', 0),
                'followers': user.get('followers', 0),
                'following': user.get('following', 0),
                'created_at': user.get('created_at', '')
            })

        page += 1

    return users

# Function to get repositories for a given user
def get_repositories(user_login):
    repos = []
    page = 1
    while True:
        response = requests.get(REPO_URL.format(user_login), headers=headers, params={'per_page': 100, 'page': page})
        data = response.json()

        if not data:
            break

        for repo in data:
            repos.append({
                'login': user_login,
                'full_name': repo['full_name'],
                'created_at': repo['created_at'],
                'stargazers_count': repo['stargazers_count'],
                'watchers_count': repo['watchers_count'],
                'language': repo['language'],
                'has_projects': repo['has_projects'],
                'has_wiki': repo['has_wiki'],
                'license_name': repo['license']['name'] if repo['license'] else ''  # Handle None case
            })

        page += 1

    return repos

# Main execution
if __name__ == "__main__":
    users = get_users()
    repositories = []

    for user in users:
        repos = get_repositories(user['login'])
        repositories.extend(repos)

    # Save to CSV files
    users_df = pd.DataFrame(users)
    repositories_df = pd.DataFrame(repositories)

    users_df.to_csv('users.csv', index=False)
    repositories_df.to_csv('repositories.csv', index=False)

    print("Data has been scraped and saved to users.csv and repositories.csv.")
