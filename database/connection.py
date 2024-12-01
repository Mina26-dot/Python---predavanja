import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="kursIT_Obuka",
        database="python"
    )

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
