#!/usr/bin/python3
"""
Reddit Subscriber Count
This script queries the Reddit API to return the number of subscribers
for a given subreddit. If an invalid subreddit is given, it returns 0.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditAPI/0.1'}
    
    # Make the GET request without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check the response status code
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscriber_count = number_of_subscribers(subreddit_name)
        print("{:d}".format(subscriber_count))

































