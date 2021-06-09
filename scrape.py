from bs4 import BeautifulSoup
import requests
from requests.api import head

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    }

url = "http://example.com"

req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.content, 'lxml')

f = open("/Users/bazilzainal/Documents/Projects/Python/scrape.txt", 'a')
f.write(soup.prettify())
f.close()


