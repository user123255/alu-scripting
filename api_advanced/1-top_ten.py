#!/usr/bin/python3
"""Module that queries the Reddit API and prints the top 10 hot posts
for a subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:alx.api:v1.0 (by /u/your_username)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
        # If subreddit is invalid, Reddit responds with 302 redirect to search
        if response.status_code == 302 or response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except (requests.exceptions.RequestException, ValueError):
        print(None)
