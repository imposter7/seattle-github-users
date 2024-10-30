import requests
import pandas as pd

# Replace 'YOUR_GITHUB_ACCESS_TOKEN' with the token you generated
headers = {"Authorization": "Bearer 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"}
def fetch_users(location="Seattle", min_followers=200, per_page=100, page=1):
    url = f"https://api.github.com/search/users?q=location:{location}+followers:>{min_followers}&per_page={per_page}&page={page}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("items", [])  # List of users on this page
    else:
        response.raise_for_status()  # Raise an error if the request fails
  def fetch_user_details(username):
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos?sort=pushed&per_page=500"
    user_data = requests.get(user_url, headers=headers).json()  # User details
    repos_data = requests.get(repos_url, headers=headers).json()  # Repositories
    return user_data, repos_data
def clean_company_name(company):
    if company:
        company = company.strip()
        if company.startswith("@"):
            company = company[1:]
        return company.upper()
    return ""
def transform_user_data(user_data):
    return {
        "login": user_data.get("login", ""),
        "name": user_data.get("name", ""),
        "company": clean_company_name(user_data.get("company", "")),
        "location": user_data.get("location", ""),
        "email": user_data.get("email", ""),
        "hireable": str(user_data.get("hireable", "")).lower(),
        "bio": user_data.get("bio", ""),
        "public_repos": user_data.get("public_repos", 0),
        "followers": user_data.get("followers", 0),
        "following": user_data.get("following", 0),
        "created_at": user_data.get("created_at", "")
    }
def transform_repo_data(repo_data, user_login):
    return {
        "login": user_login,
        "full_name": repo_data.get("full_name", ""),
        "created_at": repo_data.get("created_at", ""),
        "stargazers_count": repo_data.get("stargazers_count", 0),
        "watchers_count": repo_data.get("watchers_count", 0),
        "language": repo_data.get("language", ""),
        "has_projects": str(repo_data.get("has_projects", "")).lower(),
        "has_wiki": str(repo_data.get("has_wiki", "")).lower(),
        "license_name": repo_data.get("license", {}).get("key", "")
    }
def main():
    # Initialize lists to store data
    users_list = []
    repos_list = []

    # Fetch Seattle users with over 200 followers
    seattle_users = fetch_users()
    for user in seattle_users:
        user_details, user_repos = fetch_user_details(user["login"])
        users_list.append(transform_user_data(user_details))

        for repo in user_repos:
            repos_list.append(transform_repo_data(repo, user["login"]))

    # Save data to CSV files
    users_df = pd.DataFrame(users_list)
    repos_df = pd.DataFrame(repos_list)
    users_df.to_csv("users.csv", index=False)
    repos_df.to_csv("repositories.csv", index=False)

if __name__ == "__main__":
    main()

