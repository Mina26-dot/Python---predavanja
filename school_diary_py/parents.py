
from pythonProject.school_diary_py.connection import select_database
from pythonProject.school_diary_py.query_executor import execute_query
from pythonProject.school_diary_py.to_dict import convert_to_dict


class Parents:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_table(self):
        select_database()

        query = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ime VARCHAR(100),
                prezime VARCHAR(100),
                email VARCHAR(100)
            )
            """
        execute_query(self.table_name, query)
        print(f"Tabela {self.table_name} je kreirana.")


    def insert_parent(self, ime, prezime, email):
        query = "INSERT INTO {} (ime, prezime, email) VALUES (%s,%s,%s)"
        execute_query(self.table_name, query, params=(ime, prezime, email))

    def get_all(self):
        query = "SELECT * FROM {}"
        result = execute_query(self.table_name, query, fetch=True)

        columns = ['id', 'ime', 'prezime', 'email']
        result_dict = convert_to_dict(columns, result)
        for row in result_dict:
            print(row)

    def get_by_id(self,id):
        query = "SELECT * FROM {} WHERE id = %s"
        result = execute_query(self.table_name, query, params=(id,), fetch=True)
        columns = ['id', 'ime', 'prezime', 'email']
        result_dict = convert_to_dict(columns, result)
        print(result_dict)

    def update_parent(self, id, ime, prezime, email):
        query_check = "SELECT FROM {} WHERE id=%s"
        result = execute_query(self.table_name, query_check, params=(id,), fetch=True)

        if not result:
            print(f"Roditelj sa id-jem {id} ne postoji!")
        else:
            query = "UPDATE {} SET ime = %s, prezime = %s, email = %s"
            execute_query(self.table_name, query, params=(ime, prezime, email))
            print(f"Roditelj sa id-jem {id} je uspesno azuriran!")


    def delete_parent(self, id):
        query_check = "SELECT * FROM {} WHERE id =%s"
        result = execute_query(self.table_name, query_check, params=(id,), fetch=True)

        if not result:
            print("Roditelj sa ovim id-jem ne postoji u bazi!")
        else:
            query = "DELETE FROM {} WHERE id=%s"
            execute_query(self.table_name, query, params=(id,))
            print("Roditelj je uspesno obrisan")


parents_table = Parents("parents")
parents_table.create_table()