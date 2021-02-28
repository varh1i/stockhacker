import operator
from functools import reduce

import psycopg2
from psycopg2 import Error


class TickerDatabase:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def reset_database(self):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)

            cursor = connection.cursor()
            drop_table_query = '''
                      DROP TABLE public.ticker;
                      '''
            cursor.execute(drop_table_query)
            # SQL query to create a new table
            create_table_query = '''
                  CREATE TABLE ticker
              (TICKER VARCHAR PRIMARY KEY     NOT NULL,
                  COMPANY_NAME        VARCHAR,
                  SECTOR              VARCHAR,
                  INDUSTRY            VARCHAR,
                  PRICE               NUMERIC,
                  TARGET_PRICE_1Y     NUMERIC,
                  GROWTH_1Y           NUMERIC,
                  ACCESSIBLE          BOOLEAN,
                  UPDATE_DATE         TIMESTAMP); 
                  '''
            # Execute a command: this creates a new table
            cursor.execute(create_table_query)
            connection.commit()
            print("Table created successfully in PostgreSQL ")

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def add_tickers(self, tickers):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)

            cursor = connection.cursor()
            for ticker in tickers:
                # Executing a SQL query to insert data into  table
                insert_query = """
                INSERT INTO ticker (TICKER, GROWTH_1Y, ACCESSIBLE, UPDATE_DATE) 
                VALUES (%s, %s, %s, current_timestamp) 
                """
                item_tuple = (ticker, None, 'yes')
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

    def add_company_data(self, ticker, company_name, sector, industry):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)

            cursor = connection.cursor()
            update_query = """
            UPDATE ticker SET company_name = %s, sector = %s, industry = %s where ticker.ticker = %s 
            """
            item_tuple = (company_name, sector, industry, ticker)
            cursor.execute(update_query, item_tuple)
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def disable_company_data(self, ticker):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)

            cursor = connection.cursor()
            update_query = """
            UPDATE ticker SET accessible = %s where ticker.ticker = %s 
            """
            item_tuple = ('no', ticker)
            cursor.execute(update_query, item_tuple)
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def get_all_tickers(self):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)

            cursor = connection.cursor()
            # Executing a SQL query to insert data into  table
            select_query = """
            select ticker from ticker 
            """
            cursor.execute(select_query)
            tickers = cursor.fetchall()
            tickers = list(reduce(operator.concat, tickers))
            return tickers
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def get_all_accessible_tickers(self):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)

            cursor = connection.cursor()
            # Executing a SQL query to insert data into  table
            select_query = """
            select ticker from ticker where accessible = true and industry is null
            """
            cursor.execute(select_query)
            tickers = cursor.fetchall()
            tickers = list(reduce(operator.concat, tickers))
            return tickers
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
