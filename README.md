# Groceries

**NOTE: This is a scraping project with uses pythons open source [Scrapy Architecture](https://scrapy.org/)**

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

cd into Grocer/ and test scrapy project is active

```
$ scrapy
Scrapy 2.5.0 - project: grocer ...
```

## Architecture overview

This project uses [Scrapy](https://scrapy.org/) to obtain data from stores.

No databases have been linked yet but intends to use [SQLAlchemy](https://www.sqlalchemy.org/) to store data, and possibly [Alembic](https://alembic.sqlalchemy.org/en/latest/) for database migrations.

Overview of scrapy architecture:

![](https://docs.scrapy.org/en/latest/_images/scrapy_architecture_02.png)

