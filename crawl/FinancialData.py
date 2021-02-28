class FinancialData:

    def __init__(self, ticker, quote_table):
        self.ticker = ticker
        self.beta = quote_table[4]
        self.target_1y = quote_table[0]
        self.quote_price = quote_table[15]
        self.growth_1y = (self.target_1y / self.quote_price * 100) - 100
        self.pe = quote_table[13]
        self.eps = quote_table[7]
        self.market_cap = quote_table[11]