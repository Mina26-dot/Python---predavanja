# type : android, ios



class Product:

    number_of_products = 0
    types = ["IOS", "Android"]
    num_of_product = {
        "IOS": 0,
        "Android" : 0
    }

    def __init__(self, name,price, amount, type):

        if amount < 1:
            raise ValueError("Amount must be more than zero!")

        if type not in Product.types:
            raise ValueError("Incorrect type")


        self.name = name
        self.price = price
        self.amount = amount
        self.type = type
        Product.number_of_products += 1
        Product.num_of_product[type] += amount