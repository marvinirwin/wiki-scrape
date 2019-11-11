import re
from os import path
from bs4 import BeautifulSoup
import urllib.request

from base import base
from get_page import getPage
from get_table import getTable, getStandingCommitee

# def getPol():
# url = 'https://en.wikipedia.org/wiki/Politburo_of_the_Communist_Party_of_China'
# url =
# req = urllib.request.urlopen(url)
# article = req.read().decode()

# with open(filename, 'w') as fo:
# fo.write(article)
from templates import sectionString, staffString, baseString


def genSec():
    soup = BeautifulSoup(get('https://en.wikipedia.org/wiki/General_Secretary_of_the_Communist_Party_of_China', 'html'),
                         features='lxml')
    links = soup.find('table', {"class": "infobox"}).find('a', {"class": None})
    mep = links.attrs
    mep['src'] = getPicture(base + mep['href'])
    mep['name'] = mep['title']
    return mep


def politiburo():
    # Load article, turn into soup and get the <table>
    article = getPage('https://en.wikipedia.org/wiki/Politburo_of_the_Communist_Party_of_China', 'html')
    members = getTable(article, )
    soup = BeautifulSoup(article, 'html.parser', parser='lxml')
    members = getMembers(soup)
    for member in members:
        member['src'] = getPicture(base + member['href'])
        member['name'] = member['title']
        member['href'] = 'https://en.wikipedia.org' + member['href']
    return members

    return ''


def getMembers(soup):
    tables = soup.find_all('table', {"class": "wikitable sortable"})
    for table in tables:
        ths = table.find_all('th', scope='row')

        # For some reason wikipedia put the things we want in the th
        # However the scope is row
        def m(th):
            return th.contents[0].attrs

        r = list(map(m, ths))
        return r
    # Search through the tables for the one with the headings we want.



standingCommitteeText = ''
standingCommittee = getStandingCommitee()
for member in standingCommittee:
    standingCommitteeText += staffString.format(**member)
    standingCommitteeText += '<br>'
#content = \
    #sectionString(
        #"Standing Committee",
        #'<br>'.join(map(lambda x: staffString.format(**x), )),
    #)

open('index.html', 'w').write(
    baseString.format(body=standingCommitteeText)
)
