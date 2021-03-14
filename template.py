# hurriyet.com.tr den dolar fiyatı çekelim.

import requests
from bs4 import BeautifulSoup

hisse_url = "https://www.hurriyet.com.tr/"

html_kod = requests.get(hisse_url)

soup = BeautifulSoup(html_kod.content, 'lxml')
