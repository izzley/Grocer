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
        return self._extract(
            '''
            WITH p AS ( 
            SELECT displayname, price, savingsamount, instorewasprice, scrapetime, round(CAST(savingsamount/price*100 AS numeric), 2) AS "percent" 
            FROM woolies_test) 
            SELECT displayname, price, instorewasprice as wasprice, savingsamount as saving 
            FROM p 
            WHERE percent > 0 AND scrapetime = (SELECT MAX(scrapetime) from woolies_test);
            '''
        )
    
    def all_table(self):
        """
        Select * From woolies_test
        """
        return self._extract(
            '''
            SELECT * FROM woolies_test 
            '''
        )


    def most_recent(self):
        """
        Select * From woolies_test
        """
        return self._extract(
            '''
            SELECT * FROM woolies_test 
            WHERE scrapetime = (SELECT MAX(scrapetime) from woolies_test);
            '''
        )


    def _extract(self, arg0):
        """
        execute and fetch pyscopg2 query
        """
        query = arg0
        self.cur.execute(query)
        return self.cur.fetchall()


def _dict_to_df(dict_query):
    """
    dataframe easier to read
    """
    return pd.DataFrame(dict_query)


if __name__ == '__main__':
    
    w = WooliesView()
    # print("Current Savings")
    # print(_dict_to_df(w.current_savings()))

    print("All recent data")
    print(_dict_to_df(w.all_table()))

    # print("most recent data")
    # print(_dict_to_df(w.most_recent()))