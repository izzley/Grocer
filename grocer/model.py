from sqlalchemy import Column, Integer, Float, String, DateTime, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import BIGINT
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

    id_ = Column("id", BIGINT, primary_key=True)
    Stockcode = Column("Stockcode", String(30), primary_key=False)
    Name = Column("Name", String(100))
    DisplayName = Column("DisplayName", String(100))
    Price = Column("Price", Float)
    CupPrice = Column("CupPrice", Float)
    CupMeasure = Column("CupMeasure", String(10))
    UnitWeightInGrams = Column("UnitWeightInGrams", Float)
    WasPrice = Column("WasPrice", Float)
    InstoreWasPrice = Column("InstoreWasPrice", Float)
    SavingsAmount = Column("SavingsAmount", Float)
    url = Column("URL", String(50))
    ScrapeTime = Column("ScrapeTime", DateTime)
