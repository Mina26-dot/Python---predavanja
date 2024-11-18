import math
shops = {
    "Maxi" :{
        "Hleb" : 100,
        "Jaja" : 200
    },
    "Idea":{
        "Hleb" : 300,
        "Novine" : 120
    },
    "Roda":{
        "Novine": 40
    }
}
# print(shops["Maxi"]["Hleb"])
# print(shops["Idea"]["Hleb"])
#za nested

total_bread_price = 0
total_bread_shops = 0
max_bread_price = 0
max_bread_price_shop = " "

for shop_name, items in shops.items():
    if "Hleb" in items:
        total_bread_price += items["Hleb"]
        total_bread_shops += 1
        
        if max_bread_price < items["Hleb"]:
            max_bread_price = items["Hleb"]
            max_bread_price_shop = shop_name

# total_shops = len(shops)
average_price = total_bread_price/total_bread_shops
print(average_price)
print(max_bread_price, max_bread_price_shop)






