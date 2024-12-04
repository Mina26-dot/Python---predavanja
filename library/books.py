from pythonProject.library.connection import select_database
from query_executor import execute_query


class Books:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_table(self):
        select_database()

        query = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ime VARCHAR(100),
                kategorija VARCHAR(100),
                autor VARCHAR(100)
            )
            """
        execute_query(self.table_name, query)
        print(f"Tabela {self.table_name} je kreirana.")

    def insert(self, id, ime, kategorija, autor):
        query = f"INSERT INTO {self.table_name} (id, ime, kategorija, autor) VALUES (%s, %s, %s)"
        params = (id, ime, kategorija,autor)
        execute_query(self.table_name, query, params)


user_table = Books("knjige")
user_table.create_table()



