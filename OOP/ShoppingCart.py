
class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_product(self,item):
        self.items.append(item)

    def show_products(self):
        #imena svih proizvoda iz korpe
        for item in self.items:
            print(item.name)
