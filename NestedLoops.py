# predavanje 7.

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

# product_remove = input("Unesite proizvod: ").lower()

options = ["dodaj","obrisi","izlistaj","stop", "istorijat", "obrisi sve", "prikazi najskuplji proizvod"]
answer = None
new_product = {}
history = []


while answer not in options:
    answer = input(f"Sta zelite da uradite sa proizvodom? \n{" ".join(options)}\n").lower()

    if answer == "obrisi":
        product_remove = input("Unesite proizvod: \n").lower()
        while product_remove not in products:
            product_remove = input("Proizvod nije pronadjen! Unesite ponovo: \n").lower()

        del products[product_remove]
        msg = f"Proizvod {product_remove} je obrisan."
        print(msg)
        history.append(msg)
        answer = None


    elif answer == "dodaj":

        while True:
            new_product_name = input("Unesite ime proizvoda: \n").lower()


            if new_product_name in products:
                print(f"Proizvod {new_product_name} vec postoji! Unesite ponovo:\n")
            else:
                cena = float(input("Unesite cenu proizvoda: \n"))
                kolicina = int(input("Unesite količinu proizvoda: \n"))

                products[new_product_name] = {"cena": cena, "kolicina": kolicina}
                msg = f"Proizvod {new_product_name} je dodat!"
                print(msg)
                history.append(msg)
                answer = None
                break

    elif answer == "izlistaj":
     print(products)
     answer = None

    elif answer == "stop":
        break

    elif answer == "istorijat":
        print(history)
        answer = None
    elif answer == "obrisi sve":
        products = {}
        answer = None
 # DOMACI
    elif answer == "prikazi najskuplji proizvod":
        max_price = 0
        most_expensive_product = None
        for product in products:
            if  max_price < products[product]["cena"]:
                max_price = products[product]["cena"]
                most_expensive_product = product
                # print(max_price,most_expensive_product)
        print(products[most_expensive_product]["cena"])


    else:
        print("Neispravan unos.")





