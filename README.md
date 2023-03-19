## Product App

> The project is basically fast api product app concept to develop microservice based backend web application.

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop on
a Windows machine, but I have not documented the steps. If you've developed the apps on Windows, you should have little
problem getting up and running.

#### Setup:

- python3.10
- Fast API
- Postgres

###### Instructions:

#### Setup: 1

```bash
git clone https://github.com/mbrsagor/product.git
cd product
virtualenv venv --python=python3.10
pip install -r requirements.txt
```

#### Setup: 2

Create database using PSQL command line

```bash
sudo -u postgres psql
```

```postgresql
CREATE DATABASE product;
CREATE USER dev WITH PASSWORD '12345';
ALTER ROLE dev SET client_encoding TO 'utf8';
ALTER ROLE dev SET default_transaction_isolation TO 'read committed';
ALTER ROLE dev SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE product TO dev;
\q
```

#### Setup: 3

Migrate database:

```bash
python create_db.py
```

#### Setup: 4

Run the product if everything is alright:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
