import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
counts = tree.findall('.//count')

print "Count: ", len(counts)
Sum = sum(int(item.text) for item in counts)

print "Sum: ", Sum
