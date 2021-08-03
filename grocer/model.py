from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from grocer import settings


# https://www.jitsejan.com/scraping-with-scrapy-and-postgres


DeclarativeBase = declarative_base()


def db_connect() -> Engine:
    """
    Creates database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_items_table(engine: Engine):
    """
    Create the Items table
    """
    DeclarativeBase.metadata.create_all(engine)


class Items(DeclarativeBase):
    """
    Defines the items model
    """

    __tablename__ = "woolies_test"

    id_ = Column("id", Integer, primary_key=True)
    stockcode = Column("stockcode", String, primary_key=False)
    name = Column("name", String(100))
    displayname = Column("displayname", String(30))
    price = Column("price", Integer)
    cup_price = Column("cupprice", Integer)
    unitweight = Column("unitweight", Integer)
    wasprice = Column("wasprice", String(10))
    instorewasprice = Column("instorewasprice", Integer)
    savings_message = Column("savings_message", String(30))
    store_DOM = Column("storeDOM", String(20))
    scrape_time = Column("scrape_time", DateTime)