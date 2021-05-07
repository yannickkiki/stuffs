import pickle
import time

import pandas
import requests


def format_product(product_obj):
    size_package_type = product_obj['size']['packageType']
    size_volume = product_obj['size']['volumeSize']
    return {
        'name': product_obj['name'].title(),
        'price_original': product_obj['price']['originalPrice'],
        'price_for_sale': product_obj['price']['salePrice'],
        'size_package_type': size_package_type.title() if size_package_type else None,
        'size_volume': size_volume.title() if size_volume else None,
        'size_cup_price': product_obj['size']['cupPrice'],
        'size_cup_measure': product_obj['size']['cupMeasure'],
        'image_url': product_obj['images']['big']
    }


products_data_all = list()  # contains all the data fetched from the api
products_data_for_csv = list()  # contains the (relevant) data

pages_total_number = 2  # 37
page_size = 24  # 120

for page_number in range(1, pages_total_number + 1):
    print(f"Page: {page_number}; Fetching {page_size} products...")
    time.sleep(2)
    response = requests.get(
        url="https://shop.countdown.co.nz/api/v1/products",
        params={"target": "specials", "page": page_number, "size": page_size},
        headers={"x-requested-with": "OnlineShopping.WebApp"}
    )
    data = response.json()['products']['items']

    products_data_all += data
    products_data_for_csv += [format_product(product_obj) for product_obj in data]

    # Save current `products_data_all` in a file (so that we don't need to
    # restart the fetching from the beginning if the program crashes for some
    # reason). Do it after every `x` iterations.
    # x = 1
    # if page_number % x == 0:
    #     with open('products_data_all.sv', 'wb') as file:
    #         pickle.dump(products_data_all, file)
    #     print("Current state of `products_data_all` saved...")

# with open('products_data_all.sv', 'wb') as file:
#     pickle.dump(products_data_all, file)
# print("`products_data_all` saved...")

dataframe = pandas.DataFrame(products_data_for_csv)
dataframe.to_csv("products_data.csv", index=False)
print("Product data saved in csv file...")
