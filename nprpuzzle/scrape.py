
import requests
import urllib.request
import time
from bs4 import BeautifulSoup as Soup


PUZZLE_URL="https://www.npr.org/series/4473090/sunday-puzzle"

def scrape(url=PUZZLE_URL, puzzles=None):
    response = requests.get(url)

    soup = Soup(response.text, "html.parser")

    return soup.findAll("div", {"class": "item-info-wrap"})
