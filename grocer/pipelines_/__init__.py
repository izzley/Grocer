from sqlalchemy.orm import sessionmaker

from grocer.db import db_connect


class DatabaseStoreBase(object):
    def __init__(self):
        self.engine = engine = db_connect()
        self.session = sessionmaker(bind=engine)
