# from logging import lastResort
#
# program_name = "eclipse"
# version = 4.3
# is_new_program = False
# print(program_name, version, is_new_program)
#
# books = ["Harry Potter 1", "LOTR Collection", "Harry Potter 2"]
#
# print(books[0])
# #DOMACI

# books[0] = "Pragmatic programmer"
# books.remove("Harry Potter 2")
#
# print(books)
#
# cars = ["Audi", "BMW", "Lexus"]
# print(cars)
#
# cars[1] = "Mercedes"
# print(cars)
#
# cars.append("Skoda")
# print(cars)
#
# cars.sort()
# print(cars)
#
# print(f"Trenutno na stanju imamo {len(cars)} automobila")
#
# products = ["iPhone 14", "iPhone 15", "Samsung S23"]
# search_item = input("Unesi telefon koji zelis: ")
# if search_item in products:
#     print("Proizvod je na vasoj listi!")
# else:
#     print("Nije na vasoj listi")



# age = int(input("Unesite vase godine: "))
#
# if age < 0:
#     print("Greska!")
#     quit()
#
# if age <= 12:
#     print("Vi ste dete!")
# elif age >= 13 and age <= 18:
#     print("Vi ste tinejdzer!")
# elif age >= 18 and age <= 65:
#     print("Vi ste odrasla osoba!")
# elif age > 65:
#     print("Vi ste penzioner!")

# products = {"iPhone 14" : 999, "iPhone 15" : 1200, "samsung s23": 1220}
# search_product = input("Unesite ime proizvoda: ")
# search_product = search_product.lower()
#
# if search_product in products:
#     print(products[search_product])
# else:
#     print("Proizvod nije pronadjen!")

# students = [
#     {
#         "name" : "Mina",
#         "score" : 92,
#         "active" : True,
#     },
#    {
#         "name" : "Marko",
#         "score" : 90,
#         "active" : False,
#     },
#     {
#         "name" : "Miki",
#         "score" : 23,
#         "active" : True,
#     }
# ]
# # active_students = list()
# for active_students in students:
#     # if active_students["active"] == True: #moze i bez ==True isto je
#     if active_students["active"] == False:
#         continue
#
#     if active_students["score"] >= 80:
#              active_students["grade"] = "A"
#     elif active_students["score"] >= 60 and active_students["score"] < 80:
#                  active_students["grade"] = "B"
#     elif active_students["score"] >= 40 and active_students["score"] < 60:
#              active_students["grade"] = "C"
#     elif active_students["score"] < 40 and active_students["score"] >= 20:
#         active_students["grade"] = "D"
#     else:
#         active_students["grade"] = "F"
#     print(active_students)


# products = {
#     "hleb":{
#         "cena": 100,
#         "kolicina": 50
#     },
#     "pivo":{
#         "cena": 150,
#         "kolicina": 220
#     }
# }
# print(products)
# product_remove = input("Unesite proizvod: ").lower()
# A = None
# B = None
# answer = None
# new_product = {}
# # while product_remove not in products:
# #     print("Proizvod koji ste uneli nije pronadjen!")
# #     product_remove=input("Unesite ponovo:").lower()
# while answer not in ["a", "b"]:
#     answer = input("Sta zelite da uradite sa proizvodom? \nA: Obrisi proizvod \nB: Dodaj proizvod \n").lower()
# if answer == "a":
#   while product_remove not in products or product_remove == None:
#    product_remove=input("Proizvod nije pronadjen! Unesite ponovo:").lower()
#   if product_remove in products:
#     del products[product_remove]
#     print(f"Proizvod {product_remove} je obrisan.", products)
#   elif answer == "b":
#    while True:
#      new_product = input("Unesite ime proizvoda: ").lower()
#      if new_product in products:
#          input(f"Proizvod {new_product} vec postoji! Unesite ponovo:")
#      else:
#          cena = float(input("Unesite cenu proizvoda: "))
#          kolicina = int(input("Unesite kolicinu proizvoda: "))
#          products[new_product] = {"cena": cena, "kolicina": kolicina}
#          print(f"Proizvod {new_product} je dodat!", products)
#          break
# else:
#     print("Proizvod vec postoji!")

products = {
    "hleb": {
        "cena": 100,
        "kolicina": 50
    },
    "pivo": {
        "cena": 150,
        "kolicina": 220
    }
}

product_remove = input("Unesite proizvod: ").lower()

answer = None
new_product = {}


while answer not in ["a", "b"]:
    answer = input("Šta želite da uradite sa proizvodom? \nA: Obrisi proizvod \nB: Dodaj proizvod \n").lower()

if answer == "a":

    while product_remove not in products:
        product_remove = input("Proizvod nije pronađen! Unesite ponovo: ").lower()

    del products[product_remove]
    print(f"Proizvod {product_remove} je obrisan.", products)

elif answer == "b":

    while True:
        new_product_name = input("Unesite ime proizvoda: ").lower()


        if new_product_name in products:
            print(f"Proizvod {new_product_name} već postoji! Unesite ponovo.")
        else:
            cena = float(input("Unesite cenu proizvoda: "))
            kolicina = int(input("Unesite količinu proizvoda: "))

            products[new_product_name] = {"cena": cena, "kolicina": kolicina}
            print(f"Proizvod {new_product_name} je dodat!", products)
            break

else:
    print("Neispravan unos.")




