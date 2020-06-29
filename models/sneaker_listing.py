import sqlite3
from .orm import ORM

class SneakList(ORM):

    tablename = "snk_list"
    dbpath = ""

    def __init__(self, pk=None, snk_name="", year=0, ver_no=0, icon="", org_price=0.0,
                 curr_price=0.0, manufac="", cont_phone="", cont_email=""):
        self.pk = pk
        self.snk_name = snk_name
        self.year = year
        self.ver_no = ver_no
        self.icon = icon
        self.org_price = org_price
        self.curr_price = curr_price
        self.manufac = manufac
        self.cont_phone = cont_phone
        self.cont_email = cont_email

    def insert(self):
        # insert new row into our database
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.snk_list} (snk_name, year, ver_no, icon, org_price,
                      curr_price, manufac, cont_phone, cont_email)
                      VALUES (?,?,?,?,?,?,?,?,?);"""
            values = (self.snk_name, self.year, self.ver_no, self.icon, self.org_price
                      self.curr_price, self.manufac, self.cont_phone, self.cont_email)
            cursor.execute(sql, values)
            return True
        return False

    def update(self):
        # update row, by primary key
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.snk_list} SET snk_name=?, year=?, ver_no=?, icon=?,
                   org_price=?, curr_price=?, manufac=?, cont_phone=?, cont_email=?)
                   WHERE pk=?;"""
            values = (self.snk_name, self.year, self.ver_no, self.icon, self.org_price
                      self.curr_price, self.manufac, self.cont_phone, self.cont_email,
                      self.pk)
            cursor.execute(sql, values)
            return True
        return False

    def view_by_lister(self, cont_email):
        # view sneaker listing, by person listing      
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {self.snk_list} WHERE cont_email=?;"""
            cursor.execute(sql, (cont_email, ))
            results = cursor.fetchall()
            return results
        return []

    def view_below_price(self, given_price):
	# view sneaker listing, below a given price
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {self.snk_list}
            WHERE curr_price < given_price AND given_price=?;"""
            cursor.execute(sql, (given_price, ))
            results = cursor.fetchall()
            return results
        return []

    def view_by_manufac(self, manufac):
	# view sneaker listing, by a manufac
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {self.snk_list} WHERE manufac=?;"""
            cursor.execute(sql, (manufac, ))
            results = cursor.fetchall()
            return results
	return []

    def view_by_50below(self):
        # view sneaker listing, by below 50% original price
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {self.snk_list} WHERE curr_price <= org_price/2;"""
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        return []
