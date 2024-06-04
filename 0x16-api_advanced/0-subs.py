#!/usr/bin/python3

"""
Model working with Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of
    subscribers for a given subreddit
    """
    headers = {"User-Agent": 'u/DepartureNo8863'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
