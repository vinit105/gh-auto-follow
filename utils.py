from github import Github, GithubException
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
    """Follow a GitHub user using the authenticated account."""
    try:
        me = client.get_user()  # authenticated user
        me.add_to_following(username)
        logging.info(f"✅ Followed: {username}")
    except GithubException as e:
        logging.error(f"❌ Failed to follow {username}: {e.data.get('message') if hasattr(e, 'data') else e}")

def unfollow_user(client, username: str):
    """Unfollow a GitHub user using the authenticated account."""
    try:
        me = client.get_user()
        me.remove_from_following(username)
        logging.info(f"🚫 Unfollowed: {username}")
    except GithubException as e:
        logging.error(f"❌ Failed to unfollow {username}: {e.data.get('message') if hasattr(e, 'data') else e}")
