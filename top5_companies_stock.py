import requests
from bs4 import BeautifulSoup
import csv
import time
import random

while True:
    try:
        url = 'https://www.investing.com/equities/trending-stocks'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/41.0.2272.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content,'html.parser')

        quotes = []
        table = soup.find('div',attrs = {'id' : 'trending'})
        urlss = []
        vals = ['cost','Gain_or_loss','Gain_or_loss(in percent)']
        for row in table.findAll('div',attrs = {'class':'marketChart'}):
            quote = {'url': row.a['href']}
            urlss.append(quote)
            data = []

            for urls in urlss:
                new_url = 'https://www.investing.com'+urls['url']
                new_response = requests.get(new_url,headers=headers)
                new_soup = BeautifulSoup(new_response.content,'html.parser')
                new_table = new_soup.find('h1',attrs = {'class': 'float_lang_base_1 relativeAttr'})
                company = {'company_name': new_table.text}
                new_table = new_soup.find('div',attrs = {'class': 'top bold inlineblock'})

                for index, spans in enumerate(new_table.findAll('span', attrs= {'dir' : 'ltr'})):
                    new_soup = BeautifulSoup(str(spans),'html.parser')
                    company[vals[index]] = new_soup.span.text
                data.append(company)
                time.sleep(random.uniform(0.2, 2))
            quotes.append(data)
            try:
                if len(quotes)>1:
                    del quotes[0]
            except:
                pass
        print(quotes)
        time.sleep(random.uniform(0.2, 2))
    except:
        print('Too Much load, let me sleep')
        time.sleep(10)
