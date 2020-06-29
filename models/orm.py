class ORM:

    @classmethod
    def delete(cls, pk):
        # delete sneaker from our database, by primary key
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""DELETE FROM {cls.snk_list} WHERE pk=?;"""
            cursor.execute(sql, (pk,))
            return True
        return False

