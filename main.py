import yahoo_fin.stock_info as si
import yfinance as yf

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


def get_ticker_info():
    msft = yf.Ticker("WSO/B")
    # get stock info
    info = msft.info
    print(info)


database = TickerDatabase("docker", "docker", "127.0.0.1", "5433", "docker")
# database.reset_database()
# ticker_file_reader = TickerFileReader("resources/tickers")
# print(ticker_file_reader.tickers)
# database.add_tickers(ticker_file_reader.tickers)
tickers = database.get_all_tickers()
for ticker in tickers:
    print(ticker)
get_ticker_info()
# database.add_company_data('MSFT', "Microsoft", "Technology", "Software")



#rec = msft.recommendations
#print(msft.financials)


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

