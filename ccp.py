from os import path
from bs4 import BeautifulSoup
import urllib.request

from base import base
from get_table import getTable






# def getPol():
# url = 'https://en.wikipedia.org/wiki/Politburo_of_the_Communist_Party_of_China'
# url =
# req = urllib.request.urlopen(url)
# article = req.read().decode()

# with open(filename, 'w') as fo:
# fo.write(article)


def genSec():
    soup = BeautifulSoup(get('https://en.wikipedia.org/wiki/General_Secretary_of_the_Communist_Party_of_China', 'html'), features='lxml')
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


def getPicture(url):
    picture = get(url, 'html')
    soup = BeautifulSoup(picture, 'html.parser')
    card = getCard(soup)
    image = card.find('img')
    if image:
        image_get = image.get('src').replace('\'', '')

        replace = image_get.replace('//upload', 'https://upload')
        get(replace, '', True)
        r = replace.split('/')[-1]
        return r

    return ''



# Gets the card from a wikipedia page, the first image in this will probably be the person
def getCard(soup):
    a = soup.select('#mw-content-text > div > table.infobox.vcard')
    assert (len(a) == 1)
    card = a[0]
    return card


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




s = genSec()
string = staffString(s['name'], s['href'], s['src'])
section_string = sectionString("General Secretary", string, '')
content = \
    section_string + \
    sectionString(
        "Politiburo",
        '<br>'.join(
            map(lambda x: staffString(x['name'], x['href'], x['src']), politiburo()) \
            ),
        ''
    )

open('index.html', 'w').write(
    baseString.format(body=content)
)
