from crawl.TickerFetcher import TickerFetcher
from db.TickerDatabase import TickerDatabase

database = TickerDatabase("docker", "docker", "127.0.0.1", "5433", "docker")

all_tickers = database.get_all_accessible_tickers_by_industry('Banks—Regional')
print(all_tickers)
fetcher = TickerFetcher(database)
fetcher.fetch_all_financial(all_tickers)

'''

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

'''
target price = future eps * PE (TTM)  
'''
