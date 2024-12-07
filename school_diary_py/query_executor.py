import mysql.connector
from mysql.connector import connection
from pythonProject.school_diary_py.connection import get_connection
from pythonProject.school_diary_py import connection

def execute_query(table_name, query, params=None, fetch=False):
    connection = get_connection()
    cursor = connection.cursor()

    query = query.format(table_name)

    try:
        cursor.execute(query, params)
        if fetch:
            result = cursor.fetchall()
            return result
        else:
            connection.commit()
            print("Upit je uspesno izvrsen.")
    except mysql.connector.Error as err:
        print(f"Greska u upitu: {err}")
    finally:
        cursor.close()
        connection.close()