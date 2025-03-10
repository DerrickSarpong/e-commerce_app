import json
from sqlalchemy.orm import Session
from database import SessionLocal

import models.category as Model
from models.product import Product
from sqlalchemy.exc import IntegrityError


with open("products.json", "r") as file:
    products_data = json.load(file)

db: Session = SessionLocal()

category_names = set([product["category"] for product in products_data])
category_map = {}

for category_name in category_names:
    category = db.query(Model.Category).filter_by(name=category_name).first()
    if not category:
        category = Model.Category(name=category_name)
        db.add(category)
        db.commit()
        db.refresh(category)
    category_map[category_name] = category.id

for product in products_data:
    category_id = category_map.get(product["category"])
    new_product = Product(
        name=product["name"],
        price=product["price"],
        category_id=category_id
    )
    try:
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
    except IntegrityError:
        db.rollback()

db.close()

print("Database successfully populated with products! 🚀")