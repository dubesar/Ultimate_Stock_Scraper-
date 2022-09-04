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
        table = soup.find('div',id = 'trendingInnerContent')
        table = table.find('table',attrs = {'class' : 'genTbl closedTbl elpTbl elp20 crossRatesTbl'})
        table = table.find('tbody')
        allCountry = []
        s = ['Last','High','Low','Chg','Chg%','Vol']
        for rows in table.findAll('tr'):
            allCont = {'Name': rows.find('a').text}
            index = 0
            ignore = 0
            for row in rows.findAll('td'):
                if ignore >= 2:
                    try:
                        allCont[s[index]] = row.text
                        index+=1
                    except:
                        pass
                else:
                    ignore+=1
            allCountry.append(allCont)
            time.sleep(random.uniform(0.2,2))
        print(*allCountry)
    except:
        print('Let me sleep for some time')
        time.sleep(5)
    
