import pandas as pd
from sqlalchemy.orm import Session

from database import SessionLocal
from data_models import Products

def add_product(db: Session, brand: str, name: str, price: int, image: str, category:str):
    product = Products(brand=brand,name=name, price=price, image=image, category=category)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def main():
    db = SessionLocal()

    # Sample data for products
    products = [
        {"brand": "Coca-Cola", "name": "Original Coca-Cola 1.5L", "price": 1.5, "image": "products/coca_cola_1.5l.png", "category": "Beverages"},
        {"brand": "Lay's", "name": "Classic Potato Chips 200g", "price": 1.5, "image": "products/lays_classic_200g.png", "category": "Snacks"},
        {"brand": "Oreo", "name": "Oreo Original 154g", "price": 1.5, "image": "products/oreo_original_154g.png", "category": "Snacks"},
        {"brand": "Nestle", "name": "KitKat 4 Finger Bar 41.5g", "price": 1.5, "image": "products/kitkat_4finger_41.5g.png", "category": "Confectionery"},
        {"brand": "Heinz", "name": "Tomato Ketchup 500ml", "price": 1.5, "image": "products/heinz_ketchup_500ml.png", "category": "Condiments"},
        {"brand": "Pepsi", "name": "Pepsi Max 1.5L", "price": 1.5, "image": "products/pepsi_max_1.5l.png", "category": "Beverages"},
        {"brand": "Quaker", "name": "Quaker Oats 1kg", "price": 1.5, "image": "products/quaker_oats_1kg.png", "category": "Breakfast Foods"},
        {"brand": "Nutella", "name": "Nutella Hazelnut Spread 350g", "price": 1.5, "image": "products/nutella_350g.png", "category": "Spreads"},
        {"brand": "Tropicana", "name": "Tropicana Orange Juice 1L", "price": 1.5, "image": "products/tropicana_orange_juice_1l.png", "category": "Beverages"},
        {"brand": "Colgate", "name": "Colgate Total Toothpaste 100ml", "price": 1.5, "image": "products/colgate_total_100ml.png", "category": "Personal Care"},
        {"brand": "Tide", "name": "Tide Detergent Powder 2kg", "price": 1.5, "image": "products/tide_detergent_2kg.png", "category": "Household"},
        {"brand": "Gillette", "name": "Gillette Mach3 Razor", "price": 1.5, "image": "products/gillette_mach3_razor.png", "category": "Personal Care"},
        {"brand": "Dove", "name": "Dove Soap Bar 100g", "price": 1.5, "image": "products/dove_soap_100g.png", "category": "Personal Care"},
        {"brand": "Nescafe", "name": "Nescafe Gold Instant Coffee 200g", "price": 1.5, "image": "products/nescafe_gold_200g.png", "category": "Beverages"},
        {"brand": "Hershey's", "name": "Hershey's Chocolate Syrup 680g", "price": 1.5, "image": "products/hersheys_syrup_680g.png", "category": "Condiments"},
        {"brand": "Lipton", "name": "Lipton Green Tea 100g", "price": 1.5, "image": "products/lipton_green_tea_100g.png", "category": "Beverages"},
        {"brand": "Dettol", "name": "Dettol Antiseptic Liquid 500ml", "price": 1.5, "image": "products/dettol_500ml.png", "category": "Household"},
        {"brand": "Pringles", "name": "Pringles Original 165g", "price": 1.5, "image": "products/pringles_original_165g.png", "category": "Snacks"},
        {"brand": "Old Spice", "name": "Old Spice Deodorant 150ml", "price": 1.5, "image": "products/old_spice_deodorant_150ml.png", "category": "Personal Care"},
        {"brand": "Pantene", "name": "Pantene Shampoo 400ml", "price": 1.5, "image": "products/pantene_shampoo_400ml.png", "category": "Personal Care"},
        {"brand": "Red Bull", "name": "Red Bull Energy Drink 250ml", "price": 1.5, "image": "products/red_bull_250ml.png", "category": "Beverages"},
        {"brand": "Hellmann's", "name": "Hellmann's Mayonnaise 400g", "price": 1.5, "image": "products/hellmanns_mayo_400g.png", "category": "Condiments"},
        {"brand": "Twix", "name": "Twix Chocolate Bar 50g", "price": 1.5, "image": "products/twix_50g.png", "category": "Confectionery"},
        {"brand": "Sprite", "name": "Sprite 1.5L", "price": 1.5, "image": "products/sprite_1.5l.png", "category": "Beverages"},
        {"brand": "Knorr", "name": "Knorr Chicken Stock Cubes 80g", "price": 1.5, "image": "products/knorr_chicken_stock_80g.png", "category": "Cooking Essentials"}
    ]

    # Populate products
    for product in products:
        add_product(db, product["brand"], product["name"], product["price"], product["image"], product["category"])

    print("Data populated successfully!")

if __name__ == "__main__":
    main()