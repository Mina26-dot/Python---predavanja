from datetime import datetime
from Car import Car
from user import User

print("Opcije: "
      "\n1. Dodaj korisnika"
      "\n2. Prikazi korisnike"
      "\n3. Prikazi raspoloziva vozila"
      "\n4. Prikazi rentirana vozila")

available_options = [1, 2, 3, 4]

option = None

while option is None:
    option = input("Unesite opciju koju zelite\n")
    option = int(option)
    if option not in available_options:
        raise ValueError("Nepoznata opcija!")

    if option == 1:
        user = User()
        user.name = input("Unesite ime korisnika: ")
        user.age = int(input("Unesite godine korisnika: "))
        user.create()
        option = None

    elif option == 2:
        print(User.ALL_USERS)
        option = None

    elif option == 3 or option == 4:
        for brand in Car.VALID_CARS:
            for car in Car.VALID_CARS[brand]:
                if (not car['rented'] and option == 3) or (car['rented'] and option == 4):
                    print(car)
                    if car['rented']:
                        remaining_time = car['rented_until'] - datetime.now()
                        if remaining_time.days <= 0:
                            remaining_hours = remaining_time.seconds // 3600
                            print(f"Car {car['model']} is rented for {remaining_hours} hours.")
                        else:
                            print(f"Car {car['model']} is rented until {car['rented_until']}")
        option = None