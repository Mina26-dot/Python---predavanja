from query_executor import execute_query

class Users:
    def __init__(self, table_name):
        self.table_name = table_name

    def insert(self, ime, prezime, godine):
        query = "INSERT INTO {} (ime, prezime, godine) VALUES (%s, %s, %s)"
        execute_query(self.table_name, query, (ime, prezime, godine))

    def fetch_all(self):
        query = "SELECT * FROM {} ORDER BY godine ASC"
        result = execute_query(self.table_name, query, fetch=True)
        for row in result:
            print(row)

    def update(self, novo_ime, novo_prezime, godine, user_id):
        query = "UPDATE {} SET ime = %s, prezime = %s, godine = %s WHERE id = %s"
        execute_query(self.table_name, query, (novo_ime, novo_prezime, godine, user_id))

    def delete(self, user_id):
        query = "DELETE FROM {} WHERE id = %s"
        execute_query(self.table_name, query, (user_id,))