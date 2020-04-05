from datetime import datetime as date
from bs4 import BeautifulSoup as Soup

def lex(item):
    header = item.find('h2', {'class': 'title'}).find('a')
    teaser = item.find('p', {'class': 'teaser'})

    url = item.find('li', {'class': "audio-tool-download"}).find('a')['href']

    data = {
        'title':    header.text.replace("Sunday Puzzle: ","").strip(),
        'link':     header['href'],
        'description': teaser.find('a').contents[1],
        'guid':     url.split('?')[0],
        'file':     url.split('?')[0],
        'bytes':    [ i[5:] for i in url.split('&') if i[:5] == 'size=' ][0],
        'date':     date.strptime(teaser.find('time')['datetime'], '%Y-%m-%d'),
        'duration': item.find('b', {'class': 'audio-module-listen-duration'}).findAll('span')[1].text,
        # 'itunes:explicit': 'no',
    }
    return data
