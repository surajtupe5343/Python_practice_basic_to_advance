# Advance "sort" "sorted" functions
# sort this list of dictionaries by price.

from typing import get_origin


guitars = [

    {'model': 'faith naptune','price':50000},
    {'model': 'yamaha f310','price':8400},
    {'model': 'faith apollo venus','price':35000},
    {'model': 'taylor 814ce','price':450000}

]

print(max(guitars, key= lambda items: items['price']))
print(sorted(guitars, key= lambda items: items['price']))#---> we can use ""items.get('price')"" for ""items['price']""
print(sorted(guitars, key= lambda items: items['price'],reverse = True))
# [{'model': 'taylor 814ce', 'price': 450000}, {'model': 'faith naptune', 'price': 50000}, {'model': 'faith apollo venus', 'price': 35000}, {'model': 'yamaha f310', 'price': 
# 8400}] reversed list