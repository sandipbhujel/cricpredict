import requests
from bs4 import BeautifulSoup

url = 'http://static.cricinfo.com/rss/livexml'

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features='xml')

items = soup.findAll('item')
