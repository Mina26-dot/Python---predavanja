from django.db.models.expressions import result
from dns.e164 import query

from pythonProject.school_diary_py.connection import select_database
from pythonProject.school_diary_py.query_executor import execute_query
from pythonProject.school_diary_py.to_dict import convert_to_dict


class Subjects:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_table(self):
        select_database()

        query = f"""
             CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                naziv VARCHAR(100),
                nedeljni_fond_casova VARCHAR(100),
                nastavnik_id INT,
                razred_id INT,
                FOREIGN KEY (nastavnik_id) REFERENCES teachers(id) ON DELETE CASCADE,
                FOREIGN KEY (razred_id) REFERENCES classes(id) ON DELETE CASCADE

            )
            """
        execute_query(self.table_name, query)
        print(f"Tabela {self.table_name} je kreirana.")


    def insert_subject(self, naziv, nedeljni_fond_casova, nastavnik_id, razred_id):
        query = "INSERT INTO {} (naziv, nedeljni_fond_casova, nastavnik_id, razred_id) VALUES (%s, %s,%s,%s)"
        execute_query(self.table_name, query,params=(naziv, nedeljni_fond_casova, nastavnik_id, razred_id))

    def get_all(self):
        query = "SELECT * FROM {}"
        result = execute_query(self.table_name, query, fetch=True)

        columns = ['naziv', 'nedeljni_fond_casova', 'nastavnik_id','razred_id']
        result_dict = convert_to_dict(columns, result)
        for row in result_dict:
            print(row)


    def get_by_id(self,id):
        query = "SELECT * FROM {} WHERE id = %s"
        result = execute_query(self.table_name, query,params=(id,),fetch=True)

        columns = ['naziv', 'nedeljni_fond_casova', 'nastavnik_id', 'razred_id']
        result_dict = convert_to_dict(columns, result)
        print(result_dict)

    def update_subject(self,id, naziv, nedeljni_fond_casova, nastavnik_id, razred_id):
        query = "SELECT * FROM {} WHERE id =%s"
        result = execute_query(self.table_name, query, params=(id,))

        if not result:
            print(f"Predmet sa id-jem {id} nije pronadjen.")
        else:
            query = "UPDATE {} SET naziv = %s, nedeljni_fond_casova = %s,nastavnik_id = %s, razred_id = %s"
            execute_query(self.table_name, query, params=(naziv, nedeljni_fond_casova, nastavnik_id, razred_id))
            print(f"Predmet sa id-jem {id} je uspesno azuriran!")

    def delete_by_id(self, id):
        query = "SELECT * FROM {} WHERE id =%s"
        result = execute_query(self.table_name, query, params=(id,))

        if not result:
            print(f"Predmet sa id-jem {id} nije pronadjen!")
        else:
            query = "DELETE FROM {} WHERE id = %s"
            execute_query(self.table_name, query, params=(id,))
            print(f"Predmet sa id-jem {id} je uspesno obrisan!")


subjects_table = Subjects("subjects")
subjects_table.create_table()