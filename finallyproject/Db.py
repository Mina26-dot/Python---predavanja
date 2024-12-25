import pymysql


class Db:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="kursIT_Obuka",
            database="rent_a_car"
        )

    def get_connection(self):
        return self.connection
