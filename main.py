import requests
from bs4 import BeautifulSoup
import time
import random

# User-agent tanımlıyorum. Scraping yaparken beni browser sansın diye.
user_agent_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
                   'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1']


sembol_liste = ["AMZN", "GOOG", "FB", "NFLX", "AAPL", "MSFT"]

for sembol in sembol_liste:

    user_agent = random.choice(user_agent_list)
    agent_header = {'User-Agent': user_agent}

    hisse_url = "https://finance.yahoo.com/quote/"+sembol+"?p="+sembol+"&.tsrc=fin-srch"

    html_kod = requests.get(hisse_url, headers=agent_header)

    #print(html_kod.status_code)
    #print(html_kod.content)

    # lxml kullanmak için pip install lxml çalıştırın
    soup = BeautifulSoup(html_kod.content, 'lxml')

    #print(soup.title.text)

    sayfa_title = soup.find("title").get_text()

    #print(sayfa_title)

    header = soup.find_all('div', id='quote-header-info')[0]

    hisse_title = header.find('h1').get_text()

    #print(hisse_title)

    hisse_fiyat = header.find('div', class_='My(6px) Pos(r) smartphone_Mt(6px)').find('span').get_text()

    print('-------------------------')
    print(hisse_title + " - " + hisse_fiyat)
    print('-------------------------')

    table_info = soup.find('div', class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) "
                                         "smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY "
                                         "smartphone_Bdc($seperatorColor)")

    for i in range(0, 8):

        satirlar = table_info.find_all("tr")[i].find_all("td")

        #print(table_info)

        satir_baslik = satirlar[0].get_text()
        satir_deger = satirlar[1].get_text()

        print(satir_baslik + ": " + satir_deger)
    print('********************************')
    # 5 saniye ya da belirli bir süre bekletmezsek,
    # scraping yapan bot olduğumuzu anlayıp bloklayabilirler.
    time.sleep(5)

print('---END OF LIST---')