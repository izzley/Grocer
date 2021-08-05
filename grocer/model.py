from sqlalchemy import Column, Integer, Float, String, DateTime, create_engine
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
    stockcode = Column("stockcode", String(20), primary_key=False)
    name = Column("name", String(100))
    displayname = Column("displayname", String(30))
    price = Column("price", Integer)
    cup_price = Column("cupprice", Integer)
    cup_measure = Column("cupmeasure", String(10))
    unitweight = Column("unitweight", Float)
    wasprice = Column("wasprice", Float)
    instorewasprice = Column("instorewasprice", Float)
    savings_message = Column("savings_message", Float)
    store_DOM = Column("storeDOM", String(20))
    scrape_time = Column("scrape_time", DateTime)