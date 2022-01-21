import pandas as pd
from sqlalchemy import create_engine
from settings.scrapy import DB

DRIVER = DB['drivername']
USER = DB['username']
PASS = DB['password']
HOST = DB['host']
PORT = DB['port']
DB = DB['database']

db_string = f"{DRIVER}://{USER}:{PASS}@{HOST}:{PORT}/{DB}"

engine = create_engine(db_string)

def woolies_all():
    return pd.read_sql_query('SELECT * FROM woolies_test',
                       con=engine)

def woolies_savings():
    """
    output latest savings greater than 20%
    """
    query = '''WITH p AS (
        SELECT displayname, price, scrapetime, savingsamount, round(CAST(savingsamount/price*100 AS numeric), 2) AS "percent"
        FROM woolies_test
        )
        SELECT displayname, price, savingsamount, percent
        FROM p
        WHERE percent > 20 AND scrapetime = (SELECT MAX(scrapetime) from woolies_test);'''
    
    return pd.read_sql_query(query, con=engine)

if __name__ == "__main__":
    # print(woolies_all())
    print(woolies_savings())


# sample output of woolies_savings():
#                          displayname                         | price | savingsamount | percent 
# -------------------------------------------------------------+-------+---------------+---------
#  Minor Figures Minor Figures Barista Oat Uht Organic Milk 1l |  3.92 |          0.98 |   25.00
#  Nakula Organic Yoghurt Natural Unsweetened 1kg              |     8 |             2 |   25.00
#  Buontempo Gluten & Wheat Free Pasta Spirals Pasta 500g      |   2.7 |           0.7 |   25.93
# (3 rows)


