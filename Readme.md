# stockhacker

# TODO:

- get all company data, handle errors
- get recommendations (MSFT: 1.7 (strong buy))
- calculate 1y growth

docker build -t stock_postgresql .

docker run -p 5433:5432 --name pg_test stock_postgresql
