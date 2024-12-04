import mysql.connector

# def get_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="kursIT_Obuka",
#         database="librarypy"
#     )

import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kursIT_Obuka",
            database="librarypy"
        )
        if connection.is_connected():
            print("Povezivanje sa MySQL bazom 'librarypy' je uspesno!")
            return connection
    except Error as e:
        print(f"Greska pri povezivanju sa bazom: {e}")
        return None

def select_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("USE librarypy;")
    connection.commit()
    print("Baza 'librarypy' je sada selektovana.")
    cursor.close()
    connection.close()