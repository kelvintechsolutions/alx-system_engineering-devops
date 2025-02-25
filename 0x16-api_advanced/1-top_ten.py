#!/usr/bin/python3
'''Function that queries the Reddit API'''
import requests
from sys import argv

def top_ten(subreddit):
    '''Returns the top ten posts'''
    user = {'User-Agent': 'MyRedditBot/1.0'}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=user, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    try:
        for child in data['data']['children']:
            print(child['data']['title'])
    except KeyError:
        print(None)

if __name__ == "__main__":
    top_ten(argv[1])
