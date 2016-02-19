import urllib
import xml.etree.ElementTree as ET
import json

url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
info = json.loads(data)
comments = info['comments']
print 'Count:', len(comments)

Sum = sum(int(comment['count']) for comment in comments)
print "Sum: ", Sum
