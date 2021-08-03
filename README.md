# Groceries

**NOTE: This is a scraping project with uses pythons open source [Scrapy Architecture](https://scrapy.org/)**

Currently supports:

- Woolworths Australia https://www.woolworths.com.au/

## Requirements

 * Python 3.8+

## Quickstart

With pip + venv:

```sh
$ pip -m venv .venv
$ pip install -r requirements.txt
$ source .venv/bin/activate
```

## Development

tbc


## Architecture overview

This project uses [Scrapy](https://scrapy.org/) to obtain data from stores.

No databases have been linked yet but intends to use [SQLAlchemy](https://www.sqlalchemy.org/) to store data, and possibly [Alembic](https://alembic.sqlalchemy.org/en/latest/) for database migrations.

Overview of scrapy architecture:

![](https://docs.scrapy.org/en/latest/_images/scrapy_architecture_02.png)

