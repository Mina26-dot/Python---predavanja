import mysql.connector
from mysql.connector import connection
from pythonProject.library.connection import get_connection
from pythonProject.database import connection

def execute_query(table_name, query, params=None):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print(f"Upit za tabelu {table_name} uspesno izvrsen.")
    except mysql.connector.Error as err:
        print(f"Greska u upitu: {err}")
    finally:
        cursor.close()
        connection.close()

def check_current_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT DATABASE();")
    db = cursor.fetchone()
    print("Aktivna baza podataka:", db[0])
    cursor.close()
    connection.close()

check_current_database()