import os
import logging
from utils import get_github_client, get_followers, get_following, follow_user
from github import GithubException

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def unfollow_user(client, username: str):
    """Unfollow a GitHub user."""
    try:
        target = client.get_user(username)
        target.remove_from_following()
        logging.info(f"🚫 Unfollowed: {username}")
    except GithubException as e:
        logging.error(f"❌ Failed to unfollow {username}: {e}")

def main():
    token = os.getenv("GH_TOKEN")
    username = os.getenv("GH_USERNAME")

    if not token or not username:
        raise ValueError("Missing GH_TOKEN or GH_USERNAME in environment variables")

    client = get_github_client(token)
    followers = set(get_followers(client, username))
    following = set(get_following(client, username))

    # Follow back new followers
    to_follow = followers - following
    # Unfollow people who unfollowed you
    to_unfollow = following - followers

    if not to_follow and not to_unfollow:
        logging.info("No follow/unfollow actions needed.")
        return

    for user in to_follow:
        follow_user(client, user)

    for user in to_unfollow:
        unfollow_user(client, user)

if __name__ == "__main__":
    main()
