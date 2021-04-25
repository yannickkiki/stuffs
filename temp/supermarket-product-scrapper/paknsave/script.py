import json
import pickle
import time

from bs4 import BeautifulSoup
import pandas
import requests

products_data_for_csv = list()

category_slugs = ["fresh-foods-and-bakery"]

pages_total_number = 1  # 20
page_size = 50

for category_slug in category_slugs:
    print(f"Scraping products of category: `{category_slug}`...; {pages_total_number} pages to analyze...")
    for page_number in range(1, pages_total_number + 1):
        print(f"\tScraping products on page: {page_number}...")
        time.sleep(2)
        response = requests.get(
            url=f"https://www.paknsaveonline.co.nz/category/{category_slug}",
            params={"ps": page_size, "pg": page_number}
        )
        soup = BeautifulSoup(response.text, 'html.parser')
        product_cards = soup.find_all("div", attrs={"class": "fs-product-card"})
        for idx, product_card in enumerate(product_cards):
            print(f"Product card {idx+1}")
            badge_img = product_card.find("img")
            description_div = product_card.find("div", attrs={"class": "fs-product-card__description"})
            image_div = product_card.find("div", attrs={"class": "fs-product-card__product-image"})
            product_json_div = product_card.find(
                "div", attrs={"class": "js-product-card-footer fs-product-card__footer-container"}
            )
            product_json = json.loads(product_json_div['data-options'])
            products_data_for_csv.append({
                'description': description_div.find("h3").text.strip(),
                'description_unit': description_div.find("p").contents[0].strip(),
                'price_mode': product_json['ProductDetails']['PriceMode'],
                'price_per_item': product_json['ProductDetails']['PricePerItem'],
                'price_per_base_unit': product_json['ProductDetails']['PricePerBaseUnitText'],
                'badge': badge_img['src'].split("/")[-1].split("?")[0],
                'image_url': image_div['data-src-s']
            })


dataframe = pandas.DataFrame(products_data_for_csv)
dataframe.to_csv("products_data.csv", index=False)
print("Product data saved in csv file...")
