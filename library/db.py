import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="kursIT_Obuka",
    database="librarypy"
)

if connection.open:
    print("Connected")
else:
    print("Failed connect")