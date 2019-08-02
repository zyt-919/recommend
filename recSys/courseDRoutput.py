import pymysql


class baseio:
    db = pymysql.connect("localhost", "root", "123456", "learningrecommend")

    def open(self):
        self.cursor = self.db.cursor()

    def insert(self, data: dict):
        sql = """INSERT INTO course_dr(id,
                course_index, recommend_value)
                VALUES (%d, %d, %d)""" % (data['id'], data['course_index'], data['recommend_value'])
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def close(self):
        self.db.close()


if __name__ == "__main__":
    bbio = baseio()
    bbio.open()
    bbio.insert({'id': 123,
                 'course_index': 123,
                 'recommend_value': 123})
    bbio.close()