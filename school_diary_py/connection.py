import mysql.connector
import pymysql
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kursIT_Obuka",
            database="school_diary"

        )
        if connection.is_connected():
            print("Povezivanje sa MySQL bazom 'school_diary' je uspesno!")
            return connection
    except Error as e:
        print(f"Greska pri povezivanju sa bazom: {e}")
        return None

def select_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("USE school_diary;")
    connection.commit()
    print("Baza 'school_diary' je sada selektovana.")
    cursor.close()
    connection.close()