import operator
import time
from functools import reduce

import yahoo_fin.stock_info as si

from crawl.TickerFetcher import TickerFetcher
from db.TickerDatabase import TickerDatabase
from db.TickerFileReader import TickerFileReader


def get_growth():
    quote_table = si.get_quote_table("aapl", dict_result=False)
    print(quote_table)
    print(type(quote_table))
    one_year_estimate = quote_table.value[0]
    quote_price = quote_table.value[15]
    grow_estimate = (one_year_estimate / quote_price * 100) - 100
    print(grow_estimate)


get_growth()

'''
database = TickerDatabase("docker", "docker", "127.0.0.1", "5433", "docker")

database.reset_database()
ticker_file_reader = TickerFileReader("resources/tickers")
print(ticker_file_reader.tickers)
database.add_tickers(ticker_file_reader.tickers)


all_tickers = database.get_all_accessible_tickers()
print(all_tickers)
tickers = all_tickers  # ['MSFT', 'GOOG', '1GIS']
fetcher = TickerFetcher(database)
fetcher.fetch_all(all_tickers)

# rec = msft.recommendations
# print(msft.financials)
'''