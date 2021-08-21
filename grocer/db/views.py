import psycopg2 as pg
import pandas as pd
from settings.scrapy import DATABASE

# db credentials
db = DATABASE['database']
user = DATABASE['username']
password = DATABASE['password']

class WooliesView:
    # psycopg2 connect
    conn = pg.connect(f"dbname={db} user={user} password={password}")
    cur = conn.cursor()

    def current_savings(self):
        """
        fetchall latest savings prices. Excludes null savingsamount
        """
        query = ('''
            WITH p AS ( 
            SELECT displayname, price, savingsamount, instorewasprice, scrapetime, round(CAST(savingsamount/price*100 AS numeric), 2) AS "percent" 
            FROM woolies_test) 
            SELECT displayname, price, instorewasprice as wasprice, savingsamount as saving 
            FROM p 
            WHERE percent > 0 AND scrapetime = (SELECT MAX(scrapetime) from woolies_test);
            ''')
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def woolies_all(self):
        """
        Select * From woolies_test
        """
        query = ('''
            SELECT * FROM woolies_test
            ''')
        self.cur.execute(query)
        return self.cur.fetchall()

if __name__ == '__main__':
    # list of item tuples
    tup = WooliesView().current_savings()
    df = pd.DataFrame(tup)
    print(df)