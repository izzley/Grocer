from sqlalchemy.orm import sessionmaker

from grocer.db.model import WooliesORM, create_items_table, db_connect

from grocer.utils.pipelines import check_spider_pipeline


class StoreToWooliesDatabase:
    def __init__(self):
        engine = db_connect()
        create_items_table(engine)
        self.Session = sessionmaker(bind=engine)


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
        

