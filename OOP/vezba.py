
from Product import Product
from ShoppingCart import ShoppingCart

iPhone16 = Product("iPhone 16", 1500, 500, "IOS")
samsungS23Pro = Product("Samsung S23 Pro", 1200, 200, "Android")

phoneCart = ShoppingCart()
phoneCart.add_product(iPhone16)
phoneCart.show_products()
print(phoneCart.items)

print(Product.num_of_product)