# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
import ssl

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
pos = raw_input('Enter position: ')
# url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html"
# url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Anmol.html"
# html = urllib.urlopen(url).read()
# soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
idx = 0
while idx <= int(count):
    print "Retrieving: ", url
    scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    uh = urllib.urlopen(url, context=scontext)
    data = uh.read()
    # html = urllib.urlopen(url).read()
    soup = BeautifulSoup(data)
    tags = soup('a')
    url = tags[int(pos) - 1].get('href', None)
    idx += 1
