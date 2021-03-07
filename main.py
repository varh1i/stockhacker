import operator
import time
from functools import reduce

import yahoo_fin.stock_info as si

from crawl.TickerFetcher import TickerFetcher
from db.TickerDatabase import TickerDatabase
from db.TickerFileReader import TickerFileReader

database = TickerDatabase("docker", "docker", "127.0.0.1", "5433", "docker")
'''
database.reset_database()
ticker_file_reader = TickerFileReader("resources/tickers")
print(ticker_file_reader.tickers)
database.add_tickers(ticker_file_reader.tickers)
'''

all_tickers = database.get_all_accessible_tickers()
print(all_tickers)
tickers = all_tickers  # ['MSFT', 'GOOG', '1GIS']
# fetcher = TickerFetcher(database)
# fetcher.fetch_all(all_tickers)

# rec = msft.recommendations
# print(msft.financials)


# def print_hi(name):
#    print(f'Hi, {name}')


# https://quote-feed.zacks.com/index?t=TSLA
#resp = requests.get('https://quote-feed.zacks.com/index?t=TSLA')
#if resp.status_code != 200:
#    # This means something went wrong.
#    print('ERROR')
#stock = resp.json()
#print('Tesla: {}'.format(stock['TSLA']['last']))

#from requests_html import HTMLSession
#session = HTMLSession()
#r = session.get('https://www.zacks.com/stock/quote/AAPL?q=AAPL')
#premium_research = r.html.find('#premium_research', first=True)
#print(premium_research.html.find('dl'))

