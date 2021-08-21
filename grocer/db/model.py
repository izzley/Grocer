from datetime import datetime
from typing import List

from pydantic import BaseModel, constr
from settings import scrapy
from sqlalchemy import (CHAR, Column, DateTime, Float, Integer, String,
                        create_engine)
from sqlalchemy.dialects import postgresql
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import BIGINT

# https://pydantic-docs.helpmanual.io/usage/models/

Base = declarative_base()
metadata = Base.metadata

def db_connect() -> Engine:
    """
    Creates database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**scrapy.DATABASE))


def create_items_table(engine: Engine):
    """
    Create the Items table
    """
    Base.metadata.create_all(engine)

class WooliesORM(Base):
    """
    Defines the postgresql woolies items
    """

    __tablename__ = "woolies_test"

    id_ = Column("id", BIGINT, primary_key=True)
    stockcode = Column("stockcode", Integer, primary_key=False)
    name = Column("name", CHAR(100))
    displayName = Column("displayname", CHAR(100))
    price = Column("price", Float)
    cupprice = Column("cupprice", Float)
    cupmeasure = Column("cupmeasure", CHAR(10))
    unitweightingrams = Column("unitweightingrams", Float)
    wasprice = Column("wasprice", Float)
    instorewasprice = Column("instorewasprice", Float)
    savingsamount = Column("savingsamount", Float)
    url = Column("url", CHAR(50))
    scrapetime = Column("scrapetime", DateTime)

class WooliesModel(BaseModel):
    """
    Typing of woolies items
    """
    # @TODO pydantic types vs sql types: Integer or int
    id_: int
    Stockcode: constr(max_length=30, strict=True)
    Name: constr(max_length=100)
    DisplayName: constr(max_length=100)
    Price: float
    CupPrice: float
    CupMeasure: constr(max_length=10)
    UnitWeightInGrams: float
    WasPrice: float
    InstoreWasPrice: float
    SavingsAmount: float
    url: constr(max_length=50)
    ScrapeTime: datetime

    class Config:
        orm_mode = True
