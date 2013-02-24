import xml.etree.ElementTree as ET
tree = ET.parse('news.xml')
root = tree.getroot()

channel = root.find('channel')

for item in channel.findall('item'):
    title = item.find('title').text
    description = item.find('description').text
    link = item.find('link').text
    print title, description, link