from django.core.management.base import BaseCommand, CommandError
from news.models import Channel
import xml.etree.ElementTree as ET
import requests

def list_news(url):

    r = requests.get(url)

    root = ET.fromstring(r.text.encode('utf-8'))
    items = root.findall('channel/item')
    news = []
    for item in items:
        link = item.find('link')
        if link is not None:
            link = item.find('guid')
        news.append((item.find('title').text))
    return news

class Command(BaseCommand):
    args = '<channel_id channel_id ...>'
    help = 'Displays the latest news'

    def handle(self, *args, **options):
        for channel_id in args:
            try:
                channel = Channel.objects.get(pk=int(channel_id))
            except Channel.DoesNotExist:
                raise CommandError('Channel "%s" does not exist' % channel_id)

            titles = list_news(channel.url)
            for title in titles:
                print title

        # Downloads all news from channel.url and show the news

            self.stdout.write('Successfully loaded "%s"' % channel_id)




