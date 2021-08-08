# Groceries

**NOTE: This is a scraping project which uses pythons open source [Scrapy Architecture](https://scrapy.org/)**

Currently supports:

- Woolworths Australia https://www.woolworths.com.au/

## Requirements

 * Python 3.8+

## Quickstart

With pip + venv:

```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

Create `.pth' file pointing to project parent folder/s
```
$ echo $(pwd) >> .venv/lib/python3.8/site-packages/my_p_ext.pth
```

## Development

Check your scrapy project is active. Run the `scrapy` command from the inside the project Grocer folder:

```
$ scrapy
Scrapy 2.5.0 - project: grocer ...
```

[Scrapy Docs](https://scrapy.org/) are really comprehensive if you're interested in learning.

To connect the output data to a database, install [postgres](https://www.postgresql.org/download/) then add a filename called `grocer.ini` with database details

```
[DATABASE]
drivername = postgresql
host = localhost
port = 5432
username = <user>
password = postgres
database = <database>
```


## Architecture overview

This project uses [Scrapy](https://scrapy.org/) for webscraping and [SQLAlchemy](https://www.sqlalchemy.org/) to store the data.

Possibly will use [Alembic](https://alembic.sqlalchemy.org/en/latest/) for data migrations in the future.

Overview of scrapy architecture:

![](https://docs.scrapy.org/en/latest/_images/scrapy_architecture_02.png)

