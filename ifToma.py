# name = "Mina"
# if name == "Mina":
#     print("Hello Mina")
# else:
#     print("Hello you")
# age = 31
# if age >= 18:
#     print("Punoletni ste!")
# else:
#     print("Niste punoletni")

# name = "Admin"
# name = name.lower()
# if name == "admin":
#     print("Dobrodosao admine")
# elif name == "Mina":
#     print("Dobrodosla Mina")
# else:
#     print("Dobrodosao neko drugi")

name = "admin"
password = "sifra"

if name == "admin" and password == "sifra":
    print("Dobrodosao admine!")
elif name == "toma" and password == "123456":
    print("Dobrodosao Tomo!")
elif name == "Marija" and password == "55444":
    print("Dobrodosla Marij")
else:
    print("Niste admin! Pogresna sifra ili ime.")