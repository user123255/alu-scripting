#!/usr/bin/python3
"""
0-subs
This module contains a function that queries the Reddit API and returns
the number of subscribers for a given subreddit.

The function handles valid and invalid subreddits, sets a custom User-Agent,
and prevents redirects. Returns 0 if the subreddit does not exist.
"""

import requests  # Alphabetical import


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers if valid subreddit, else 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:subscribers:v1.0 (by /u/wintermancer)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return 0
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except (requests.RequestException, ValueError):
        return 0
