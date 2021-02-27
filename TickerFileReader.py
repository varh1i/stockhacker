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

    def save_to_tinydb(self, path):
        db = TinyDB(path)
        for ticker in self.tickers:
            db.insert({'ticker': ticker, 'growth_1y': 'NaN'})
        return db

    def save_to_postgres_db(self):
        try:
            connection = psycopg2.connect(user="docker",
                                          password="docker",
                                          host="127.0.0.1",
                                          port="5433",
                                          database="docker")

            cursor = connection.cursor()
            for ticker in self.tickers:
                # Executing a SQL query to insert data into  table
                insert_query = """
                INSERT INTO ticker (TICKER, GROWTH_1Y, UPDATE_DATE) 
                VALUES (%s, %s, current_timestamp) 
                """
                item_tuple = (ticker, None)
                cursor.execute(insert_query, item_tuple)
                connection.commit()
                print("1 Record inserted successfully")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

