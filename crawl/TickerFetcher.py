import time
import yahoo_fin.stock_info as si
import yfinance as yf

from crawl.FinancialData import FinancialData
from crawl.TickerData import TickerData


class TickerFetcher:

    def __init__(self, ticker_database):
        self.database = ticker_database

    def fetch_all(self, all_tickers):
        tickers = all_tickers
        for i in range(len(tickers)):
            ticker = tickers[i]
            ticker_data = self.get_ticker_info(ticker)
            if ticker_data is not None:
                self.database.add_company_data(
                    ticker_data.ticker,
                    ticker_data.company_name,
                    ticker_data.sector,
                    ticker_data.industry)
                print("Company data added for %s [%d/%d]" % (ticker, i + 1, len(tickers)))
            else:
                self.database.disable_company_data(ticker)

    def fetch_all_financial(self, all_tickers):
        tickers = all_tickers
        for i in range(len(tickers)):
            ticker = tickers[i]
            fd = self.get_financial_data(ticker)
            if fd is not None:
                self.database.add_financial_data(
                    ticker, fd.beta, fd.target_1y, fd.quote_price, fd.growth_1y, fd.pe, fd.eps,
                    fd.market_cap)
                print("Financial data added for %s [%d/%d]" % (ticker, i + 1, len(tickers)))
            else:
                print("Financial data NOT added for %s [%d/%d]" % (ticker, i + 1, len(tickers)))

    @staticmethod
    def get_ticker_info(ticker_code):
        try:
            ticker_data = yf.Ticker(ticker_code)
            # get stock info
            info = ticker_data.info
            if ticker_data is not None:
                return TickerData(ticker_code, info)
            else:
                return None
        except(Exception, KeyError) as error:
            print("Error while trying to fetch data for %s" % ticker_code, error)

    @staticmethod
    def get_financial_data(ticker):
        quote_table = si.get_quote_table(ticker, dict_result=False)
        print(quote_table)
        print(type(quote_table))
        return FinancialData(ticker, quote_table)