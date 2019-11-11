from bs4 import BeautifulSoup
from base import base
from get_image import getImage, getImageFromPage
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
    return {
        # Xi Jinping
        'personName': el.get('title'),
        #'/wiki/File:Xi_Jinping_2016.jpg'
        'personPageHref': base + el.get('href'),
        'imageHref': getImageFromPage(base + el.get('href'))
    }


def getStandingCommitee():
    return getTable(
        'https://en.wikipedia.org/wiki/Politburo_Standing_Committee_of_the_Communist_Party_of_China',
        '#mw-content-text > div > table.wikitable > tbody > tr > td:nth-child(4) > a',
        lambda x: True,
        getGoodProps
    )


# v = getStandingCommitee()
