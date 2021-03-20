#hurriyet.com.tr den dolar çekilecek


import requests
from bs4 import BeautifulSoup

hisse_url = "https://bigpara.hurriyet.com.tr/altin/"

html_kod = requests.get(hisse_url)


soup = BeautifulSoup(html_kod.content, 'lxml')

bilgi_bar = soup.find_all('div', class_='dovizBar mBot10')[0].find_all('a')[1].find_all('span')

print(bilgi_bar[1].get_text())
print(bilgi_bar[4].get_text())
print(bilgi_bar[5].get_text())
print(bilgi_bar[6].get_text())