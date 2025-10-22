import os
import logging
from utils import (
    get_github_client,
    get_followers,
    get_following,
    follow_user,
    unfollow_user,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def main():
    token = os.getenv("GH_TOKEN")
    username = os.getenv("GH_USERNAME")

    if not token or not username:
        raise ValueError("Missing GH_TOKEN or GH_USERNAME in environment variables")

    client = get_github_client(token)
    followers = set(get_followers(client, username))
    following = set(get_following(client, username))

    to_follow = followers - following
    to_unfollow = following - followers

    if not to_follow and not to_unfollow:
        logging.info("No follow/unfollow actions needed.")
        return

    for user in to_follow:
        follow_user(token, user)

    for user in to_unfollow:
        unfollow_user(token, user)

if __name__ == "__main__":
    main()
