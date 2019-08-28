nQueensChallenge
================
[![Build Status](https://travis-ci.com/allanstone/nQueensChallenge.svg?branch=master)](https://travis-ci.com/allanstone/nQueensChallenge)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-secrets)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This project resolves the eight queens puzzle: [problem description](https://en.wikipedia.org/wiki/Eight_queens_puzzle).<br/>
It uses a Postgres db to store the results wrapped by SqlAlchemy API, tested via pytest module and some plugins for db fixtures and mocking.
Also it it uses Travis for CI, alembic for migrations and all the solution is dockerized within docker compose.

## Prerequisites
You can run only the sollution algorithm with python3 or install as a whole with [docker-compose](https://docs.docker.com/compose/install/)
* pytest, sqlalchemy, psycopg2 

## Installation
I strongly recomend to use a virtual enviroment to install the
```
git clone https://github.com/allanstone/nQueensChallenge.git .
pip install -r requirements.txt #run as standalone script without db
python main.py <number-of-queens>
```
## Installation with Docker
```
git clone https://github.com/allanstone/nQueensChallenge.git
cd nQueensChallenge/
docker-compose up -d
docker logs #results should be there!
```

## Database
The database url is configured on ``config.py`` it can be easily changed for production or another db
```
DATABASE_URI = 'postgres+psycopg2://postgres:post123@localhost:5432/testdb'
```

## Migrations
Project uses alembic to manage migrations script
http://alembic.zzzcomputing.com/en/latest/

### Example usage 
Add new migrations with
```
alembic revision --autogenerate -m "migration name"
```
Upgrade your database with
```
alembic upgrade head
```

## Tests
Running the tests, using diferent flags from the fixtures, aviod warning due 'postgres' dialect name has been renamed to 'postgresql'
```
py.test  nQueensChallenge/tests/ --sqlalchemy-connect-url="postgres+psycopg2://postgres:post123@localhost:5432/testdb" -p no:warnings -v
py.test --sqlalchemy-config-file nQueensChallenge/tests/test_db.py  -p no:warnings -v
py.test  nQueensChallenge/tests/test_db.py  -p no:warnings -v

```

## Optimizations
* Add code coverage with coveralls or codecov
* Use a tool like tox-travis to test diferent python versions
* Deploy a more consistent architecture for microservices (e.g using kubernetes or docker swarm)

