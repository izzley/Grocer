import pandas as pd
from sqlalchemy import create_engine
from grocer.settings import DATABASE

USER = DATABASE['drivername']
PASS = DATABASE['password']
HOST = DATABASE['host']
PORT = DATABASE['port']
DB = DATABASE['database']

db_string = f"postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}"

engine = create_engine(db_string)

df = pd.read_sql_query('SELECT * FROM items',
                       con=engine)
print(df.to_string())
