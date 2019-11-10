import urllib
from os import path


def getImage(url):
    # get the filename from the url
    filename = url.split('/')[-1]
    # check that we've not already requested and saved it
    if not path.exists(filename):
            try:
                # use urlretrieve, I had trouble with wget.download
                # (I think it didnt like the user agent
                str = urllib.request.urlretrieve(url, filename)
            except Exception:
                print("exception getting image: " + url)
                return ''

            open(filename, 'w').write(str)
            return str
    return open(filename).read()

