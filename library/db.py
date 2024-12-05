import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="kursIT_Obuka",
    database="librarypy",
    cursorclass=pymysql.cursors.DictCursor

)

if connection.open:
    print("Connected")
else:
    print("Failed connect")