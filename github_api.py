import requests

from config import (
    BASE_GITHUB_API,
    GITHUB_TOKEN
)

# ==========================================================
# Request Headers
# ==========================================================

HEADERS = {}

if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# ==========================================================
# Get User Information
# ==========================================================

def get_user(username):

    url = f"{BASE_GITHUB_API}/users/{username}"

    response = requests.get(
        url,
        headers=HEADERS
    )

    if response.status_code != 200:

        print("Status Code :", response.status_code)
        print(response.text)

        raise Exception("GitHub user not found.")

    return response.json()


# ==========================================================
# Get Public Repositories
# ==========================================================

def get_repositories(username):

    url = f"{BASE_GITHUB_API}/users/{username}/repos"

    response = requests.get(
        url,
        headers=HEADERS
    )

    if response.status_code != 200:

        raise Exception(
            "Unable to fetch repositories."
        )

    return response.json()


# ==========================================================
# Get Repository Commits
# ==========================================================

def get_commits(username, repo_name):

    url = (
        f"{BASE_GITHUB_API}"
        f"/repos/{username}/{repo_name}/commits"
    )

    response = requests.get(
        url,
        headers=HEADERS
    )

    if response.status_code == 409:

        print(
            f"Skipping '{repo_name}' (Repository is empty)"
            )
        return []

    elif response.status_code == 404:

        print(
            f"Skipping '{repo_name}' (Repository not found)"
        )

        return []

    elif response.status_code != 200:

        print(
            f"Skipping '{repo_name}' (HTTP {response.status_code})"
        )

        return []

    commits = response.json()

    commit_data = []

    for commit in commits:

        commit_data.append({

            "repository": repo_name,

            "sha": commit["sha"],

            "message": commit["commit"]["message"],

            "date": commit["commit"]["author"]["date"]

        })

    return commit_data


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    username = input(
        "Enter GitHub Username: "
    )

    # -------------------------------
    # User Details
    # -------------------------------

    user = get_user(username)

    print("\nDeveloper")
    print("=" * 50)

    print("Name :", user["name"])
    print("Username :", user["login"])
    print("Followers :", user["followers"])
    print("Public Repositories :", user["public_repos"])

    # -------------------------------
    # Repository List
    # -------------------------------

    repos = get_repositories(username)

    print("\nRepositories")
    print("=" * 50)

    for repo in repos:

        print(repo["name"])

    # -------------------------------
    # Test First Repository Commits
    # -------------------------------

    if repos:

        repo_name = repos[0]["name"]

        print("\n" + "=" * 50)
        print("Testing Repository :", repo_name)
        print("=" * 50)

        commits = get_commits(
            username,
            repo_name
        )

        print("\nFirst 5 Commits\n")

        for commit in commits[:5]:

            print("-" * 50)

            print("Repository :", commit["repository"])
            print("Date       :", commit["date"])
            print("Message    :", commit["message"])
            print("SHA        :", commit["sha"][:10])

    else:

        print("\nNo repositories found.")