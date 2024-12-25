from Db import Db


class User(Db):
    ALL_USERS = []

    def __init__(self):
        super().__init__()
        self.__age = None
        self.__name = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Godine moraju biti minimum 18!")

        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        split_name = new_name.split()

        if len(split_name) < 2:
            raise ValueError("Name must be in format first last name!")

        self.__name = new_name

    def create(self):
        if self.__name is None or self.__age is None:
            raise ValueError("Name or age are not set")

        with self.connection.cursor() as cursor:
            query = "INSERT INTO users (name, age) VALUES (%s, %s)"
            cursor.execute(query, (self.__name, self.__age))
            self.connection.commit()

        User.ALL_USERS.append([self.__name, self.__age])
