import datetime
import pymysql
from pymysql import cursors
from pythonProject.finallyproject.Db import Db

class Car(Db):
    VALID_CARS = {
        "Audi": [
            {"model": "A4", "production_year": 2004, "rented": False, "rented_until": None},
            {"model": "A5", "production_year": 2003, "rented": False, "rented_until": None},
            {"model": "A6", "production_year": 2002, "rented": False, "rented_until": None}
        ],
        "BMW": [
            {"model": "M5", "production_year": 2010, "rented": False, "rented_until": None},
            {"model": "M3", "production_year": 2008, "rented": False, "rented_until": None}
        ],
        "Mercedes": [
            {"model": "GLK", "production_year": 2015, "rented": False, "rented_until": None},
            {"model": "GLE", "production_year": 2017, "rented": False, "rented_until": None}
        ]
    }

    def __init__(self):
        super().__init__()
        self.__brand = None
        self.__model = None
        self.__production_year = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__brand is None:
            raise ValueError("Brand must be set!")

        valid_models = [car['model'] for car in Car.VALID_CARS[self.__brand]]

        if model not in valid_models:
            raise ValueError("Model is not valid!")

        self.__model = model

        for car_model in Car.VALID_CARS[self.__brand]:
            if car_model['model'] == model:
                self.__production_year = car_model['production_year']

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if brand not in Car.VALID_CARS:
            raise ValueError("Invalid car")

        self.__brand = brand

    @property
    def production_year(self):
        return self.__production_year

    @production_year.setter
    def production_year(self, year):
        if self.__model is None:
            raise ValueError("Production year cannot be set!")

        if self.__model is not None and self.__production_year is not None:
            raise ValueError("Production year cannot be set!")

        self.__production_year = year

    def rent_car(self,car_id, rented_until):
        connection = Db().get_connection()
        with connection.cursor() as cursor:
            query = "UPDATE cars SET rented = TRUE, rented_until = %s WHERE id = %s"
            cursor.execute(query, (rented_until, car_id))
            connection.commit()

    def load_cars_from_db(self):
        connection = Db().get_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = "SELECT * FROM cars"
            cursor.execute(query)
            result = cursor.fetchall()

            for row in result:
                brand = row['brand']
                model = row['model']
                production_year = row['production_year']
                rented = row['rented']
                rented_until = row['rented_until']

                if brand not in Car.VALID_CARS:
                    Car.VALID_CARS[brand] = []
                Car.VALID_CARS[brand].append({
                    "model": model,
                    "production_year": production_year,
                    "rented": rented,
                    "rented_until": rented_until
                })

    def display_rented_cars(self):
        connection = Db().get_connection()
        with connection.cursor(cursors.DictCursor) as cursor:
            query = "SELECT * FROM cars WHERE rented = TRUE"
            cursor.execute(query)
            rented_cars = cursor.fetchall()
            for car in rented_cars:
                rented_until = car['rented_until']
                if rented_until is not None:
                    remaining_time = rented_until - datetime.datetime.now()
                    if remaining_time.days < 0:
                        remaining_hours = remaining_time.seconds // 3600
                        print(f"Car {car['model']} is rented for {remaining_hours} hours.")
                    else:
                        print(f"Car {car['model']} is rented until {rented_until.strftime('%Y-%m-%d %H:%M:%S')}")
                else:
                    print(f"Car {car['model']} is currently rented with no return date set.")
