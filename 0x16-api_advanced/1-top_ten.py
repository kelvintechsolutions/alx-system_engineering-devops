#!/usr/bin/python3
'''Function that queries the Reddit API'''
import requests
from sys import argv

def top_ten(subreddit):
    '''Returns the top ten posts'''
    # Set a proper User-Agent to comply with Reddit's API guidelines
    headers = {
        'User-Agent': 'Lizzie-Script/1.0 (by /u/your_reddit_username)'
    }
    
    # Construct the API URL
    url = f'https://www.reddit.com/r/{subreddit}/top/.json?limit=10'
    
    try:
        # Make the GET request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code != 200:
            print(None)
            return
        
        # Parse the JSON response
        data = response.json()
        
        # Extract the list of posts
        posts = data.get('data', {}).get('children', [])
        
        # Ensure there are posts
        if not posts:
            print(None)
            return
        
        # Print the titles of the first 10 posts
        for post in posts[:10]:
            title = post.get('data', {}).get('title', None)
            print(title)
            print('---')  # Optional: Print a separator between titles
            
    except requests.exceptions.RequestException as e:
        # Handle request errors (e.g., timeout, connection error)
        print("Request failed:", str(e))
        print(None)
    except ValueError as e:
        # Handle JSON parsing errors
        print("JSON parsing failed:", str(e))
        print(None)
    except Exception as e:
        # Handle other unexpected errors
        print("An error occurred:", str(e))
        print(None)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python3 script.py <subreddit>")
        exit(1)
    top_ten(argv[1])
