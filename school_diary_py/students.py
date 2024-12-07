
from pythonProject.school_diary_py.connection import select_database
from pythonProject.school_diary_py.query_executor import execute_query
from pythonProject.school_diary_py.to_dict import convert_to_dict


class Students:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_table(self):
        select_database()

        query = f"""
             CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ime VARCHAR(100),
                prezime VARCHAR(100),
                roditelj_id INT,
                razred_id INT,
                FOREIGN KEY (roditelj_id) REFERENCES parents(id) ON DELETE CASCADE,
                FOREIGN KEY (razred_id) REFERENCES classes(id) ON DELETE CASCADE

            )
            """
        execute_query(self.table_name, query)
        print(f"Tabela {self.table_name} je kreirana.")

    def insert_student(self,ime, prezime, roditelj_id, razred_id):
        query="INSERT INTO {} (ime, prezime, roditelj_id, razred_id) VALUES (%s, %s, %s, %s)"
        execute_query(self.table_name, query, (ime, prezime, roditelj_id, razred_id))

    def get_all_students(self):
        query = "SELECT * FROM {}"
        result = execute_query(self.table_name, query, fetch=True)

        columns = ['id', 'ime', 'prezime', 'roditelj_id', 'razred_id']
        result_dict = convert_to_dict(columns, result)
        for row in result_dict:
            print(row)

    def get_by_id(self, id):
        query = "SELECT * FROM {} WHERE id = %s"
        result = execute_query(self.table_name, query, params=(id,), fetch=True)

        columns = ['id', 'ime', 'prezime', 'roditelj_id', 'razred_id']
        result_dict = convert_to_dict(columns, result)
        print(result_dict)

    def update_student(self, id, ime, prezime, roditelj_id, razred_id):
        query_check = "SELECT * FROM {} WHERE id = %s"
        result = execute_query(self.table_name, query_check, params=(id,))

        if not result:
            print(f"Ucenik sa id-jem {id} ne postoji!")
        else:
            query = "UPDATE {} SET ime = %s, prezime = %s, roditelj_id = %s, razred_id = %s WHERE id = %s"
            execute_query(self.table_name, query, params=(ime, prezime, roditelj_id, razred_id, id))
            print(f"Ucenik sa id-jem {id} je uspesno azuriran")



    def delete_student(self,id):
        check_query = "SELECT * FROM {} WHERE id = %s"
        result = execute_query(self.table_name, check_query, params=(id,), fetch=True)

        if not result:
            print(f"Ucenik sa id-jem {id}  ne postoji u bazi")
        else:
            query = "DELETE FROM {} WHERE id = %s"
            execute_query(self.table_name, query, params=(id,))
            print("Ucenik je uspesno obrisan!")

students_table = Students("students")
students_table.create_table()