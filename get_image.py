import request
from os import path
from bs4 import BeautifulSoup
from get_page import getPage
from sanitize_filename import sanitize


def getImage(url):
    # get the filename from the url
    filename = sanitize(url.split('/')[-1])
    # check that we've not already requested and saved it
    if not path.exists(filename):
        try:
            # use urlretrieve, I had trouble with wget.download
            # (I think it didnt like the user agent
            response = request(url)
            str = response.content

        except Exception:
            print("exception getting image: " + url)
            return ''

        open(filename, 'w').write(str)
        return str

    return open(filename, 'rb').read()


def getImageFromPage(url):
    picture = getPage(url)
    soup = BeautifulSoup(picture, 'html.parser')
    images = soup.select('#mw-content-text > div > table.infobox.vcard > tbody > tr:nth-child(3) > td > a > img')

    if len(images):
        image = images[0]
        image_get = image.get('src').replace('\'', '')
        replace = image_get.replace('//upload', 'https://upload')
        getImage(replace)
        r = replace.split('/')[-1]
        return sanitize(r)
    return ''
