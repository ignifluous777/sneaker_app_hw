import sqlite3
import os

PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, "sneaker_list.db")
print(DATAPATH)

def schema():
    with sqlite3.connect(DATAPATH) as conn:
        cursor = conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS list (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                snk_name VARCHAR,
                year INTEGER,
                ver_no INTEGER,
                icon VARCHAR,
                org_price FLOAT,
                curr_price FLOAT,
                manufac VARCHAR,
                cont_phone VARCHAR,
                cont_email VARCHAR
              )"""

        cursor.execute(sql)

if __name__ == "__main__":
    schema()
