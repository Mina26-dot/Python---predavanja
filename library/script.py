import random
from datetime import datetime
from fileinput import close
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


insert_book_and_author(connection)


# def insert_user(con, ime, dob):
#     cursor = con.cursor()
#
#     users_query = "INSERT INTO korisnici(ime, dob) VALUES (%s,%s)"
#     cursor.execute(users_query, (ime, dob))
#     con.commit()
#     cursor.close()
#
# def insert_book(con, name, genre, author):
#     cursor = con.cursor()
#
#     query = "INSERT INTO knjige(ime, kategorija, autor) VALUES (%s, %s, %s)"
#     cursor.execute(query, (name, genre, author))
#     con.commit()
#     cursor.close()


# insert_user(connection, "Mina Minic", "1993-09-08")
# insert_book(connection, "Neka knjiga", "Nesto", "Janko Janic")


# generate_book_title(connection)




# domaci
# generate_author -> faker.name()
# generate_book_title -> ? -> ime knjige

# -> generisi ime auotra
# -> generisi ime knjige
# -> insertuj knjigu
# -> insertuj autora (usera)