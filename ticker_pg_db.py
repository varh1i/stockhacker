import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="docker",
                                  password="docker",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="docker")

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''
          CREATE TABLE ticker
      (TICKER INT PRIMARY KEY     NOT NULL,
          INDUSTRY           VARCHAR,
          GROWTH_1Y           NUMERIC,
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
