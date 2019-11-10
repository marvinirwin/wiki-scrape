import request
from os import path

import requests


def getPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

    filename = url.split('/')[-1]
    # If a wikipedia article doesn't explicitly end with nedsWith, ignore it
    # if not filename.endsWith('.html'):
    filename += '.html'

    if not path.exists(filename):
        response = requests.get(url, headers=headers)
        str = response.content
        open(filename, 'w').write(str.decode('utf8'))
        return str
        print("exception getting url: " + url)
        return ''

    return open(filename).read()
