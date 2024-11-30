import mysql.connector
from mysql.connector import connection
from pythonProject.database.main import execute_query
from pythonProject.database import main


class Users:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def __get_connection(self):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return connection

    def execute_query(self, query, values=None, fetch=False):
        connection = self.__get_connection()
        cursor = connection.cursor()

        cursor.execute(query, values)

        if fetch:
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        else:
            connection.commit()
            cursor.close()
            connection.close()


def create_table():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kursIT_Obuka",
        database="python"
    )

    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ime VARCHAR(100),
        prezime VARCHAR(100),
        godine INT
    );
    """


    cursor.execute(create_table_query)
    print("Tabela 'users' je uspesno kreirana.")

    cursor.close()
    connection.close()

def insert_user(table_name,ime, prezime, godine):
    query = "INSERT INTO {} (ime,prezime,godine) VALUES (%s,%s,%s)"
    execute_query(table_name,query, (ime, prezime, godine))


def fetch_all_users(table_name):
    query = "SELECT * FROM {} ORDER BY godine DESC"
    result = execute_query(table_name, query, fetch=True)
    for row in result:
        print(row)

def update_user(table_name, novo_ime, novo_prezime, godine,user_id):
    query = "UPDATE {} SET ime = %s, prezime = %s, godine = %s WHERE id = %s"
    execute_query(table_name, query, (novo_ime, novo_prezime, godine, user_id))


def delete_user(table_name,user_id):
        query = "DELETE FROM {} WHERE id = %s"
        execute_query(table_name, query, (user_id,))

# Vec sam pre nego sto sam stigla do domaceg odradila ovako pa nisam menjala parametre. Zato saljem ovako

insert_user("users","Mina", "Nina", 31)
fetch_all_users("users")