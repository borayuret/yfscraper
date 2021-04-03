# hurriyet.com.tr den dolar fiyatı çekelim.

import requests
from bs4 import BeautifulSoup
import ortak

hisse_url = "https://www.trendyol.com/vestel/kmi-9701-g-kurutma-makinesi-p-77471681?boutiqueId=555729&merchantId=107179"

html_kod = requests.get(hisse_url)

soup = BeautifulSoup(html_kod.content, 'lxml')

bilgi_bar = soup.find('div', class_='pr-bx-nm with-org-prc').find_all('span')

#print(bilgi_bar)

fiyat = bilgi_bar[1].get_text()

print(fiyat)

print(ortak.fiyat_temizle(fiyat))
