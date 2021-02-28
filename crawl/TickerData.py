class TickerData:

    def __init__(self, ticker, ticker_data):
        self.ticker = ticker
        if 'shortName' in ticker_data:
            self.company_name = ticker_data['shortName']
        elif 'longName' in ticker_data:
            self.company_name = ticker_data['longName']
        else:
            self.company_name = ''
        if 'sector' in ticker_data:
            self.sector = ticker_data['sector']
        else:
            self.sector = ''
        if 'industry' in ticker_data:
            self.industry = ticker_data['industry']
        else:
            self.industry = ''
