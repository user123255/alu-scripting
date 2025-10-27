#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles
of the first 10 hot posts of a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Prints:
        The titles of the first 10 hot posts, or None if invalid.
    """
    if not isinstance(subreddit, str) or not subreddit:
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditAPI/0.1'}
    params = {'limit': 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            print(None)
            return

        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
