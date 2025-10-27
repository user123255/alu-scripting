#!/usr/bin/python3
"""
Return and print the titles of the first 10 hot posts for a given subreddit
using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot posts.

    Args:
        subreddit (str): The subreddit to query.

    Prints:
        The titles of the first 10 hot posts, or None if invalid subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Reddit-Task/0.1"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )

        # Check for invalid subreddit or HTTP error
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            print(None)
            return

        # Print the first 10 hot post titles
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)

