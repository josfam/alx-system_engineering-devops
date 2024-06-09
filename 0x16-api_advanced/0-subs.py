#!/usr/bin/python3

"""Fetches the number of subscribers in a subreddit"""

import sys
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers in the provided subreddit.
    Returns 0 if the subreddit does not exist
    """
    subreddit = sys.argv[1]
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    custom_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,\
         like Gecko) Chrome/125.0.0.0 Safari/537.36'
    headers = {'user-agent': custom_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 404:  # non-existent subreddit
        return 0
    r_data = r.json().get('data')
    return r_data.get('subscribers')
