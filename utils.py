from github import Github
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def get_github_client(token: str):
    """Initialize and return a GitHub client."""
    return Github(token)

def get_followers(client, username: str):
    """Fetch list of usernames who follow the given user."""
    user = client.get_user(username)
    return [f.login for f in user.get_followers()]

def get_following(client, username: str):
    """Fetch list of usernames that the user already follows."""
    user = client.get_user(username)
    return [f.login for f in user.get_following()]

def follow_user(client, username: str):
    """Follow a GitHub user."""
    try:
        target = client.get_user(username)
        target.add_to_following()
        logging.info(f"✅ Followed: {username}")
    except Exception as e:
        logging.error(f"❌ Failed to follow {username}: {e}")
