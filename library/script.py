import random
from datetime import datetime
from db import connection
from pythonProject.library.db import connection

print(connection)
from faker import Faker

faker = Faker()


# zanr: Misterija, Avantura
# Imenica: Tajna, Zamak
# Pridevi: Zaboravljena


# Misterija Zaboravljenog Zamka: Napisao faker.name()

genres = ["Mistery", "Adventure", "Fantasy"]
adjectives = ["Dark", "Forbidden", "Mysterious", "Hidden", "Eternal"]
nouns = ["Secrets" , "Kingdom", "Journey", "Love", "Shadow"]

def generate_random_dob():
    dob = faker.date_between(start_date=datetime(1950, 1, 1), end_date=datetime(2000, 1, 1))
    return dob

def generate_random_genre():
    return random.choice(genres)

def generate_author(con):
    author_name = faker.name()
    # dob = faker.date_between(start_date=datetime(1950, 1, 1), end_date=datetime(2000, 1, 1))
    dob = generate_random_dob()
    return author_name, dob


def generate_book_title(con):
    genre = generate_random_genre()
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)

    author_name, dob = generate_author(con)

    book_name = f"{adjective} {noun}: A {genre} story by {author_name}"
    return book_name, author_name, dob

def insert_book_and_author(con):
    book_name, author_name, dob = generate_book_title(con)

    cursor = con.cursor()

    insert_author_query = """
    INSERT INTO korisnici (ime, dob)
    VALUES (%s, %s)
    """
    cursor.execute(insert_author_query, (author_name, dob))
    author_id = cursor.lastrowid

    insert_book_query = """
    INSERT INTO knjige (ime, kategorija, autor)
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_book_query, (book_name, generate_random_genre(),author_id))


    con.commit()
    cursor.close()


def get_all_books(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM knjige")
    con.commit()
    results = cursor.fetchall()
    cursor.close()
    return results

def get_book_by_ID(con,book_id):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM knjige WHERE id = %s", book_id)
    con.commit()
    results = cursor.fetchone()
    cursor.close()
    return results

def delete_book_by_ID(con,book_id):
    cursor = con.cursor()
    cursor.execute("DELETE FROM knjige WHERE id = %s", book_id)
    con.commit()
    cursor.close()

choice = None

while choice is None:
    choice = input("Sta zelite da uradite? \n 1. Napravi random knjigu \n 2. Prikazi knjige \n 3. Prikazi knjigu po ID \n 4. Obrisi knjigu po ID: \n")
    print(choice)

    if choice == "1":
        insert_book_and_author(connection)
    elif choice == "2":
        books = get_all_books(connection)
        for book in books:
         print(book)
    elif choice == "3":
        book_id = None
        while book_id is None:
            book_id = int(input("Unesite ID knjige: \n"))

            book = get_book_by_ID(connection,book_id)

            if book:
                print(f"Ime ove knjige je: {book['ime']}")
            else:
                print("Knjiga ne postoji, pokusajte ponovo!")
                book_id = None

    elif choice == "4":
        book_id = None
        while book_id is None:
            book_id = int(input("Unesite ID knjige: "))

            delete_book_by_ID(connection,book_id)

    else:
        choice = None

