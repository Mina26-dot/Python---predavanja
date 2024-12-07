from pythonProject.school_diary_py.connection import select_database
from pythonProject.school_diary_py.query_executor import execute_query
from pythonProject.school_diary_py.to_dict import convert_to_dict


class Teachers:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_table(self):
        select_database()

        query = f"""
             CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ime VARCHAR(100),
                prezime VARCHAR(100)

            )
            """
        execute_query(self.table_name, query)
        print(f"Tabela {self.table_name} je kreirana.")

    def insert_teacher(self, ime, prezime):
        query = "INSERT INTO {} (ime, prezime) VALUES (%s, %s)"
        execute_query(self.table_name, query, params=(ime, prezime))

    def get_all(self):
        query = "SELECT * FROM {}"
        result = execute_query(self.table_name, query, fetch=True)

        columns = ['id', 'ime', 'prezime']
        result_dict = convert_to_dict(columns, result)
        for row in result_dict:
            print(row)


    def get_by_id(self, id):
        query = "SELECT * FROM {} WHERE id = %s"
        result = execute_query(self.table_name, query, params=(id,), fetch=True)

        columns = ['id', 'ime', 'prezime']
        result_dict = convert_to_dict(columns, result)
        print(result_dict)

    def update_teacher(self, ime, prezime):
        query = "SELECT * FROM {} WHERE id =%s"
        result = execute_query(self.table_name, query, params=(id,))

        if not result:
            print(f"Nastavnik sa id-jem {id} nije pronadjen.")
        else:
            query = "UPDATE {} SET ime = %s, prezime = %s"
            execute_query(self.table_name, query, params=(ime, prezime))
            print(f"Nastavnik sa id-jem {id} je uspesno azuriran!")

    def delete_by_id(self, id):
        query = "SELECT * FROM {} WHERE id =%s"
        result = execute_query(self.table_name, query, params=(id,))

        if not result:
            print(f"Nastavnik sa id-jem {id} nije pronadjen!")
        else:
            query = "DELETE FROM {} WHERE id = %s"
            execute_query(self.table_name, query, params=(id,))
            print(f"Nastavnik sa id-jem {id} je uspesno obrisan!")

teachers_table = Teachers("teachers")
teachers_table.create_table()