from tinydb import TinyDB
import psycopg2


class TickerFileReader:
    def __init__(self, path):
        self.tickers = []
        f = open(path, "r")
        lines = f.readlines()
        for i in range(len(lines)):
            if i > 0:
                self.tickers.append(lines[i].split()[0])
        self.tickers = list(dict.fromkeys(self.tickers))

    def save_to_tinydb(self, path):
        db = TinyDB(path)
        for ticker in self.tickers:
            db.insert({'ticker': ticker, 'growth_1y': 'NaN'})
        return db
