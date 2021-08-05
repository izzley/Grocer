# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker

from grocer.model import Items, create_items_table, db_connect


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# @TODO create database pipeline
class GrocerPipeline:
    def __init__(self):
        engine = db_connect()
        create_items_table(engine)
        self.Session = sessionmaker(bind=engine)
    
    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        session = self.Session()
        instance = session.query(Items).filter_by(**item).one_or_none()
        if instance:
            return instance
        woolies = Items(**item)

        try:
            session.add(woolies)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
