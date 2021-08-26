from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from grocer.db.model import WooliesORM, create_items_table, db_connect

from grocer.utils.pipelines import check_spider_pipeline


def get_db_session() -> Engine:
    """
    Connect to the database.
    """
    engine = db_connect()
    create_items_table(engine)
    return sessionmaker(bind=engine)


class StoreToWooliesDatabase:
    def __init__(self) -> None:
        self.Session = get_db_session()


    @check_spider_pipeline
    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        session = self.Session()
        instance = session.query(WooliesORM).filter_by(**item).one_or_none()
        if instance:
            return instance
        woolies = WooliesORM(**item)

        try:
            session.add(woolies)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


class HarrisfarmItems:
    @check_spider_pipeline
    def process_item(self, item, spider):
        """
        Process harris farm items with xpath tags
        """
        pass
        

