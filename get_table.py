from bs4 import BeautifulSoup

from base import base
from get_image import getImage
from get_page import getPage


def getTable(url, rowSelector, filterFunc, getFunc):
    # Load article, turn into soup and get the <table>
    article = getPage(url)
    soup = BeautifulSoup(article, 'html.parser')
    els = soup.select(rowSelector)
    results = []
    for el in els:
        if filterFunc(el):
            results.append(getFunc(el))

    return results



def getGoodProps(el):
    # getImage is implemented in another file, it will fetch the image and return a proper href
    el['src'] = getImage(base + el['href'])
    el['href'] = 'https://en.wikipedia.org' + el['href']

print(getTable(
    'https://en.wikipedia.org/wiki/Politburo_Standing_Committee_of_the_Communist_Party_of_China',
    '#mw-content-text > div > table.wikitable > tbody > tr > td:nth-child(2) > div > div > a',
    lambda x: True,
    getGoodProps
))
