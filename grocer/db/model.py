from typing import List

from pydantic import BaseModel, constr
from datetime import datetime
from sqlalchemy import Column, DateTime, Float, Integer, CHAR, String, create_engine
from sqlalchemy.dialects import postgresql
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import BIGINT

from grocer import settings

# https://pydantic-docs.helpmanual.io/usage/models/

Base = declarative_base()

# def db_connect() -> Engine:
#     """
#     Creates database connection using database settings from settings.py.
#     Returns sqlalchemy engine instance
#     """
#     return create_engine(URL(**settings.DATABASE))


# def create_items_table(engine: Engine):
#     """
#     Create the Items table
#     """
#     Base.metadata.create_all(engine)

class WooliesORM(Base):
    """
    Defines the postgresql woolies items
    """

    __tablename__ = "woolies_test"

    id_         = Column("id", BIGINT, primary_key=True)
    Stockcode   = Column("Stockcode", CHAR(30), primary_key=False)
    Name        = Column("Name", CHAR(100))
    DisplayName = Column("DisplayName", CHAR(100))
    Price       = Column("Price", Float)
    CupPrice    = Column("CupPrice", Float)
    CupMeasure  = Column("CupMeasure", CHAR(10))
    UnitWeightInGrams = Column("UnitWeightInGrams", Float)
    WasPrice    = Column("WasPrice", Float)
    InstoreWasPrice = Column("InstoreWasPrice", Float)
    SavingsAmount = Column("SavingsAmount", Float)
    url         = Column("URL", CHAR(50))
    ScrapeTime  = Column("ScrapeTime", DateTime)

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