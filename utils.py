import requests
import logging
from github import Github

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

API_BASE = "https://api.github.com"

def get_github_client(token: str):
    return Github(token)

def get_followers(client, username: str):
    user = client.get_user(username)
    return [f.login for f in user.get_followers()]

def get_following(client, username: str):
    user = client.get_user(username)
    return [f.login for f in user.get_following()]

def follow_user(token: str, username: str):
    """Follow a GitHub user through REST API."""
    url = f"{API_BASE}/user/following/{username}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    r = requests.put(url, headers=headers)
    if r.status_code in (204, 304):
        logging.info(f"✅ Followed: {username}")
    else:
        logging.error(f"❌ Failed to follow {username}: {r.status_code} {r.text}")

def unfollow_user(token: str, username: str):
    """Unfollow a GitHub user through REST API."""
    url = f"{API_BASE}/user/following/{username}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    r = requests.delete(url, headers=headers)
    if r.status_code in (204, 304):
        logging.info(f"🚫 Unfollowed: {username}")
    else:
        logging.error(f"❌ Failed to unfollow {username}: {r.status_code} {r.text}")
