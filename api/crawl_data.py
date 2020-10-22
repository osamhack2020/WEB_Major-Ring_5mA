#api for crawling
from urllib.request import urlopen
# import re
# import requests
from bs4 import BeautifulSoup

def show_activity(url):
    soup = BeautifulSoup(urlopen(url),"html.parser")
    return str(soup.select("div.tit > a"))

print(show_activity("https://wevity.com"))