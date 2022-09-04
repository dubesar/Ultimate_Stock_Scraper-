from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

while True:
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.investing.com/equities/trending-stocks')
        res = driver.execute_script("return document.documentElement.outerHTML")

        driver.quit()

        soup = BeautifulSoup(res,'lxml')
        soup = soup.find('div',attrs = {'class':'trendingStocks'})
        for row in soup.findAll('div',attrs = {'class' : 'chartContainer'}):
            try:
                soup = row.find('div',attrs = {'class':'dirLtr trendingStocksChart','id':'trendingBySectorChart'})
                soup = soup.find('div',attrs = {'id':'highcharts-2','class':'highcharts-container'})
                soup = soup.find('svg',attrs = {'style':'font-family:"Lucida Grande", "Lucida Sans Unicode", Arial, Helvetica, sans-serif;font-size:12px;'})
                soup = soup.find('g',attrs = {'class':'highcharts-axis-labels highcharts-xaxis-labels'})

                company = [[rows.text] for rows in soup.findAll('text')]
                print(company)
            except:
                pass
    except:
        print('Let me sleep for some time')
        time.sleep(random.uniform(0.2,5))
