#!/usr/bin/python3

"""Prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    custom_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    headers = {
        'user-agent': custom_user_agent
    }
    # for the query string
    params = {'limit': 9}
    r = requests.get(
        url, headers=headers, params=params, allow_redirects=False)
    if r.status_code == 404:
        print('None')
    r_data = r.json().get('data')
    for child in r_data.get('children'):
        print(child.get('data').get('title'))
