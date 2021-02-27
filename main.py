import yahoo_fin.stock_info as si
import operator
from tinydb import TinyDB, Query
from TickerFileReader import TickerFileReader

ticker_file_reader = TickerFileReader("resources/tickers")
print(ticker_file_reader.tickers)
ticker_file_reader.save_to_postgres_db()
#Ticker = Query()
#search = db.search(Ticker.ticker == '1GIS')
#print('test')
#print(search)


def get_increase(ticker):
    return 1.0

def addToList(my_dict, name, value):
    my_dict[name] = value
    return my_dict


my_dict = {}
addToList(my_dict, "MSFT", 10.2)
addToList(my_dict, "AAPL", 15.2)

sorted_d = dict( sorted(my_dict.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_d)

"""
quote_table = si.get_quote_table("aapl", dict_result=False)
#print(quote_table)
one_year_estimate = quote_table.value[0]
quote_price = quote_table.value[15]
grow_estimate = (one_year_estimate / quote_price * 100) - 100
print(grow_estimate)
"""
#import yfinance as yf

#msft = yf.Ticker("MSFT")

# get stock info
#info = msft.info
#print(info)

#rec = msft.recommendations
#print(msft.financials)

import requests


#def print_hi(name):
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

# print_hi('PyCharm')
