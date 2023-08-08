#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot/.json?\
            limit=50&after={}".format(subreddit, after)
    headers = {"User-Agent": 'My Agent'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()['data']
        after = posts['after']
        posts = posts['children']

        for post in posts:
            hot_list.append(post['data']['title'])

            if after is not None:
                recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
