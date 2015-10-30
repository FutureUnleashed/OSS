import re
import urllib2,sys
import BeautifulSoup
from BeautifulSoup import NavigableString
address = 'http://towerofthehand.com/reference/index/a.html'
html = urllib2.urlopen(address).read()

soup = BeautifulSoup(html)

try:
	charactersDiv = soup.find('div',attrs={'class':'keygrid'})
	charactersNameTRs = charactersDiv.findall('a')
	for link in charactersNameTRs:
		print link
except IOError:
	print 'io error'
