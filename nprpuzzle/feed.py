import datetime
import PyRSS2Gen as RSS2

FEED_DATA = {
    'title': 'Sunday Puzzle',
    'link':  'npr.org/puzzle',
    'description': "The Weekly Quiz from NPR Puzzlemaster Will Shortz",

    'lastBuildDate': datetime.datetime.now(),

    'image': RSS2.Image(
        url = 'https://willshortz.com/images/Shortz_Will.jpg',
        title = 'Will Shortz',
        link  = 'npr.org/puzzle'
    ),

    'ttl': 24*60,
    'language': 'en-US',
    'generator': None,
    'docs': None,
}

def feed(items, data=FEED_DATA):
    return RSS2.RSS2(
        **data,
        items = [RSS2.RSSItem(
            title = i['title'],
            link  = i['link'],
            description = i['description'],
            guid  = RSS2.Guid(i['guid']),
            enclosure = RSS2.Enclosure(url=i['file'], type='audio/mpeg', length=i['bytes']),
            pubDate = i['date'],
        ) for i in items ]
    )
