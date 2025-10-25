#!/usr/bin/python3
"""
0-subs
Module that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given
    subreddit.

    Args:
        subreddit (str): Name of the subreddit.

    Returns:
        int: Number of subscribers. Returns 0 if subreddit is invalid.
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
