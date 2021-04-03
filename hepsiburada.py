# hurriyet.com.tr den dolar fiyatı çekelim.

import requests
from bs4 import BeautifulSoup

hisse_url = "https://www.hepsiburada.com/caykur-filiz-1000-gram-p-ZYHPCAYKUDCY023?magaza=Günaysa"

html_kod = requests.get(hisse_url)

soup = BeautifulSoup(html_kod.content, 'lxml')

bilgi_bar = soup.find('div', class_='product-price-wrapper')

print(bilgi_bar)