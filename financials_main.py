import yahoo_fin.stock_info as si

from crawl.FinancialData import FinancialData
from db.TickerDatabase import TickerDatabase


def get_financial_data(ticker):
    quote_table = si.get_quote_table(ticker, dict_result=False)
    print(quote_table)
    print(type(quote_table))
    return FinancialData(ticker, quote_table)


database = TickerDatabase("docker", "docker", "127.0.0.1", "5433", "docker")

ticker = 'AAPL'
fd = get_financial_data(ticker)
database.add_financial_data(ticker, fd.beta, fd.target_1y, fd.quote_price, fd.growth_1y, fd.pe, fd.eps, fd.market_cap)

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
