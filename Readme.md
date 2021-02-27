# stockhacker

docker build -t stock_postgresql .

docker run -p 5433:5432 --name pg_test stock_postgresql
