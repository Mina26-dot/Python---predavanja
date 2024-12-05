from datetime import datetime
from pythonProject.library.books import faker
from pythonProject.library.connection import select_database
from query_executor import execute_query

class Users:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_table(self):

        select_database()

        query = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ime VARCHAR(100),
                dob DATE
            )
            """
        execute_query(self.table_name, query)
        print(f"Tabela {self.table_name} je kreirana.")

    def insert(self, con, ime, dob):
        query = f"INSERT INTO {self.table_name} (ime, dob) VALUES (%s, %s, %s)"
        params = (ime, dob)
        execute_query(self.table_name, query, params)





# user_table = Users("korisnici")
# user_table.create_table()


