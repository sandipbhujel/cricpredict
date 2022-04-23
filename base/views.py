from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def room(request):
    return render(request, 'base/room.html')

def test(request):
    url = 'http://static.cricinfo.com/rss/livexml'

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features='xml')

    items = soup.findAll('item')
    matches_items = []
    for item in items:
        match_item = {}
        match_item['title'] = item.title.text
        match_item['description'] = item.description.text
        matches_items.append(match_item)
        match = matches_items[0]
    return render(request, 'base/live.html')