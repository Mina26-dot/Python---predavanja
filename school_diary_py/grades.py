from pythonProject.school_diary_py.connection import select_database
from pythonProject.school_diary_py.query_executor import execute_query
from pythonProject.school_diary_py.to_dict import convert_to_dict


class Grades:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_table(self):
        select_database()

        query = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ocena INT,
                usmeni INT,
                pismeni INT,
                vladanje INT,
                prvo_polug INT,
                drugo_polug INT,
                zakljucna_ocena INT,
                nastavnik_id INT,
                ucenik_id INT,
                FOREIGN KEY (nastavnik_id) REFERENCES teachers(id) ON DELETE CASCADE,
                FOREIGN KEY (ucenik_id) REFERENCES students(id) ON DELETE CASCADE
            )
            """
        execute_query(self.table_name, query)
        print(f"Tabela {self.table_name} je kreirana.")

    def insert_grade(self, ocena, usmeni, pismeni, vladanje, prvo_polug, drugo_polug, zakljucna_ocena, nastavnik_id, ucenik_id):
        query = "INSERT INTO {} (ocena, usmeni, pismeni, vladanje, prvo_polug, drugo_polug, zakljucna_ocena, nastavnik_id, ucenik_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        execute_query(self.table_name, query, params=(ocena, usmeni, pismeni, vladanje, prvo_polug, drugo_polug, zakljucna_ocena, nastavnik_id, ucenik_id))

    def get_all(self):
        query = "SELECT * FROM {}"
        result = execute_query(self.table_name, query, fetch=True)

        columns = ['id', 'ocena', 'usmeni', 'pismeni', 'vladanje', 'prvo_polug',
                   'drugo_polug', 'zakljucna_ocena','nastavnik_id', 'ucenik_id']
        result_dict = convert_to_dict(columns, result)
        for row in result_dict:
            print(row)

    def get_by_id(self,id):
        query = "SELECT * FROM {} WHERE id = %s"
        result = execute_query(self.table_name, query, params=(id,), fetch=True)

        columns = ['id', 'ocena', 'usmeni', 'pismeni', 'vladanje', 'prvo_polug',
                   'drugo_polug', 'zakljucna_ocena', 'nastavnik_id', 'ucenik_id']
        result_dict = convert_to_dict(columns, result)
        print(result_dict)

    def update_grade(self,ocena, usmeni, pismeni, vladanje, prvo_polug,
                     drugo_polug, zakljucna_ocena, nastavnik_id, ucenik_id):
        query_check = "SELECT FROM {} WHERE id=%s"
        result = execute_query(self.table_name, query_check, params=(id,), fetch=True)

        if not result:
            print(f"Ocena sa id-jem {id} ne postoji!")
        else:
            query = ("UPDATE {} SET ocena = %s, usmeni = %s, pismeni = %s vladanje =%s, prvo_polug = %s, "
                     "drugo_polug = %s, zakljucna_ocena = %s, nastavnik_id =%s, razred_id = %s")
            execute_query(self.table_name, query, params=(ocena, usmeni, pismeni, vladanje, prvo_polug,
                                                          drugo_polug, zakljucna_ocena, nastavnik_id, ucenik_id))
            print(f"Ocena sa id-jem {id} je uspesno azurirana")

    def delete_grade(self, id):
        query_check = "SELECT * FROM {} WHERE id =%s"
        result = execute_query(self.table_name, query_check, params=(id,), fetch=True)

        if not result:
            print(f"Ocena sa id-jem {id} ne postoji u bazi!")
        else:
            query = "DELETE FROM {} WHERE id=%s"
            execute_query(self.table_name, query, params=(id,))
            print("Ocena je uspesno obrisana")

grades_table = Grades("grades")
grades_table.create_table()