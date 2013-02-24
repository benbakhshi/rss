import xml.etree.ElementTree as ET
import requests

rsslist = []
feeds = ['http://www.11alive.com/rss/local/3/10.xml','http://www.nba.com/bucks/rss.xml','http://www.python.org/channews.rdf']

for feed in feeds:
	rsslist.append(requests.get(feed))

for rss in rsslist:
	root = ET.fromstring(rss.text.encode('utf-8'))	
	items = root.findall('channel/item')
	# print items
	news = []
	for item in items[:3]:
		link = item.find('link')
		if not link:
			link = item.find('guid')
		news.append((item.find('title').text, link.text))
	print news





