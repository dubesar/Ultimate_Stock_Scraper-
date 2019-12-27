## Ultimate_Stock_Scraper

The following files contains scraping the stock price by different ways

##### 1. Scraping top stocks:
``` 
python3 top5_companies_stock.py
```

##### 2. Scraping stocks by quotes 'PRICE'
```
python3 top_stock_quotes_price.py
```

Similarly it can be done for Performance , Technical , Fundamental. Since this is dynamic using selenium to change the Javascript bar to other options of Performance , Technical , Fundamental


##### 3. Scraping stocks by chart ( Popularity )
```
python3 trending_Stocks_by_popularity.py
```

Here the whole chart is not extracted but the x_axis and the value of each bar using Selenium

##### 4. Scraping stocks by chart ( Sector )
```
python3 trending_stocks_by_sector.py
```

Here similar to the previous is done.

All the data recorded is dynamically scraped from the website with some time lag.

### Tech Used:

1. Selenium

2. Beuatiful Soup

3. Python
