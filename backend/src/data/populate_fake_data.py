import pandas as pd
from sqlalchemy.orm import Session

from database import SessionLocal
from data_models import Products

def add_product(db: Session, brand: str, name: str, quantity:str, price: int, image: str, category:str):
    product = Products(brand=brand,name=name, quantity=quantity, price=price, image=image, category=category)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def main():
    db = SessionLocal()

    # Sample data for products
    products = [
        {"brand": "Coca-Cola", "name": "Original Coca-Cola 1.5L", "quantity": "1.5L", "price": 2.0, "image": "products/coca_cola_1.5l.png", "category": "Beverages"},
        {"brand": "Coca-Cola", "name": "Coca-Cola Zero Sugar 1.5L", "quantity": "1.5L", "price": 2.1, "image": "products/coca_cola_zero_1.5l.png", "category": "Beverages"},
        {"brand": "Coca-Cola", "name": "Original Coca-Cola 500ml", "quantity": "500ml", "price": 1.5, "image": "products/coca_cola_500ml.png", "category": "Beverages"},
        {"brand": "Coca-Cola", "name": "Coca-Cola Diet 1.5L", "quantity": "1.5L", "price": 2.0, "image": "products/coca_cola_diet_1.5l.png", "category": "Beverages"},
        {"brand": "Coca-Cola", "name": "Coca-Cola Cherry 1.5L", "quantity": "1.5L", "price": 2.2, "image": "products/coca_cola_cherry_1.5l.png", "category": "Beverages"},
        {"brand": "Coca-Cola", "name": "Coca-Cola Vanilla 500ml", "quantity": "500ml", "price": 1.8, "image": "products/coca_cola_vanilla_500ml.png", "category": "Beverages"},
        {"brand": "Coca-Cola", "name": "Original Coca-Cola Can 330ml", "quantity": "330ml", "price": 1.0, "image": "products/coca_cola_can_330ml.png", "category": "Beverages"},
        {"brand": "Coca-Cola", "name": "Coca-Cola Zero Sugar Can 330ml", "quantity": "330ml", "price": 1.1, "image": "products/coca_cola_zero_can_330ml.png", "category": "Beverages"},
        {"brand": "Coca-Cola", "name": "Coca-Cola Caffeine Free 1.5L", "quantity": "1.5L", "price": 2.1, "image": "products/coca_cola_caffeine_free_1.5l.png", "category": "Beverages"},
        {"brand": "Coca-Cola", "name": "Coca-Cola Diet Can 330ml", "quantity": "330ml", "price": 1.05, "image": "products/coca_cola_diet_can_330ml.png", "category": "Beverages"},
        {"brand": "Lay's", "name": "Classic Potato Chips 200g", "quantity": "200g", "price": 2.5, "image": "products/lays_classic_200g.png", "category": "Snacks"},
        {"brand": "Oreo", "name": "Oreo Original 154g", "quantity": "154g", "price": 2.0, "image": "products/oreo_original_154g.png", "category": "Snacks"},
        {"brand": "Nestle", "name": "KitKat 4 Finger Bar 41.5g", "quantity": "41.5g", "price": 1.8, "image": "products/kitkat_4finger_41.5g.png", "category": "Confectionery"},
        {"brand": "Nestle", "name": "Nestle Pure Life Water 500ml", "quantity": "500ml", "price": 1.0, "image": "products/nestle_pure_life_500ml.png", "category": "Beverages"},
        {"brand": "Nestle", "name": "Nescafe Gold 200g", "quantity": "200g", "price": 10.0, "image": "products/nescafe_gold_200g.png", "category": "Beverages"},
        {"brand": "Nestle", "name": "Nestle Milo Can 240ml", "quantity": "240ml", "price": 1.6, "image": "products/nestle_milo_240ml.png", "category": "Beverages"},
        {"brand": "Nestle", "name": "Maggi 2-Minute Noodles Chicken 75g", "quantity": "75g", "price": 1.2, "image": "products/maggi_noodles_chicken_75g.png", "category": "Food"},
        {"brand": "Nestle", "name": "Nestle Coffee-Mate 450g", "quantity": "450g", "price": 4.5, "image": "products/nestle_coffee_mate_450g.png", "category": "Beverages"},
        {"brand": "Nestle", "name": "KitKat Chunky 50g", "quantity": "50g", "price": 2.0, "image": "products/kitkat_chunky_50g.png", "category": "Confectionery"},
        {"brand": "Nestle", "name": "Nestle Cheerios 375g", "quantity": "375g", "price": 4.5, "image": "products/nestle_cheerios_375g.png", "category": "Cereals"},
        {"brand": "Nestle", "name": "Smarties Tube 38g", "quantity": "38g", "price": 1.5, "image": "products/smarties_tube_38g.png", "category": "Confectionery"},
        {"brand": "Nestle", "name": "Nescafe Classic 100g", "quantity": "100g", "price": 5.0, "image": "products/nescafe_classic_100g.png", "category": "Beverages"},
        {"brand": "Nestle", "name": "Nestle Fitness Cereal 375g", "quantity": "375g", "price": 4.8, "image": "products/nestle_fitness_cereal_375g.png", "category": "Cereals"},
        {"brand": "Nestle", "name": "Nestle Nesquik Powder 300g", "quantity": "300g", "price": 4.0, "image": "products/nesquik_powder_300g.png", "category": "Beverages"},
        {"brand": "Nestle", "name": "Nestle Lactogen 1 Infant Formula 400g", "quantity": "400g", "price": 7.0, "image": "products/nestle_lactogen_400g.png", "category": "Baby Food"},
        {"brand": "Nestle", "name": "Maggi Tomato Ketchup 500g", "quantity": "500g", "price": 2.5, "image": "products/maggi_ketchup_500g.png", "category": "Condiments"},
        {"brand": "Nestle", "name": "KitKat White Chocolate 41.5g", "quantity": "41.5g", "price": 1.9, "image": "products/kitkat_white_41.5g.png", "category": "Confectionery"},
        {"brand": "Nestle", "name": "Nestle NAN Optipro 1 400g", "quantity": "400g", "price": 8.0, "image": "products/nan_optipro_400g.png", "category": "Baby Food"},
        {"brand": "Nestle", "name": "Nescafe Dolce Gusto Cappuccino Pods 16s", "quantity": "16s", "price": 7.0, "image": "products/dolce_gusto_cappuccino_16s.png", "category": "Beverages"},
        {"brand": "Nestle", "name": "Nestle Milkybar White Chocolate 25g", "quantity": "25g", "price": 1.5, "image": "products/milkybar_25g.png", "category": "Confectionery"},
        {"brand": "Nestle", "name": "Maggi Masala Noodles 70g", "quantity": "70g", "price": 1.0, "image": "products/maggi_masala_noodles_70g.png", "category": "Food"},
        {"brand": "Nestle", "name": "Nestle Cerelac Wheat & Honey 400g", "quantity": "400g", "price": 5.0, "image": "products/cerelac_wheat_honey_400g.png", "category": "Baby Food"}
    ]


    # Populate products
    for product in products:
        add_product(db, product["brand"], product["name"], product["quantity"], product["price"], product["image"], product["category"])

    print("Data populated successfully!")

if __name__ == "__main__":
    main()