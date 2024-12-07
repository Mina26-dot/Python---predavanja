from pythonProject.school_diary_py.connection import select_database
from pythonProject.school_diary_py.query_executor import execute_query
from pythonProject.school_diary_py.to_dict import convert_to_dict


class Classes:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_table(self):
        select_database()

        query = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                razred INT,
                odeljenje VARCHAR(100)
            )
            """
        execute_query(self.table_name, query)
        print(f"Tabela {self.table_name} je kreirana.")

    def insert_class(self,razred, odeljenje):
        query="INSERT INTO {} (razred, odeljenje) VALUES (%s, %s)"
        execute_query(self.table_name, query, (razred, odeljenje))

    def get_all(self):
        query = "SELECT * FROM {}"
        result = execute_query(self.table_name, query, fetch=True)

        columns = ['id', 'razred', 'odeljenje']
        result_dict = convert_to_dict(columns, result)
        print(result_dict)


    def get_by_id(self,id):
        query = "SELECT * FROM {} WHERE id = %s"
        result = execute_query(self.table_name, query, params=(id,), fetch=True)
        if not result:
            print(f"Razred po id-jem {id} ne postoji!")
        else:
            columns = ['id', 'razred', 'odeljenje']
            result_dict = convert_to_dict(columns, result)
            print(result_dict)

    def update_by_id(self, id, razred, odeljenje):
        query_check = "SELECT FROM {} WHERE id=%s"
        result = execute_query(self.table_name, query_check, params=(id,), fetch=True)

        if not result:
            print(f"Razred sa ovim id-jem {id} ne postoji!")
        else:
            query = "UPDATE {} SET razred = %s, odeljenje = %s"
            execute_query(self.table_name, query, params=(razred, odeljenje))
            print(f"Razred sa id-jem {id} je uspesno azuriran!")

    def delete_by_id(self,id):
        query_check = "SELECT * FROM {} WHERE id = %s"
        result = execute_query(self.table_name, query_check, params=(id,), fetch=True)

        if not result:
            print(f"Razred sa id-jem {id} ne postoji.")
        else:
            query = "DELETE FROM {} WHERE id = %s"
            execute_query(self.table_name, query, params=(id,))
            print(f"Razred sa id-jem {id} je uspesno obrisan!")


classes_table = Classes("classes")
classes_table.create_table()