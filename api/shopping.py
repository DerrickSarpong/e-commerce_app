from typing import List
from random import choice

from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import async_get_db, get_db
import pydantic_schema.shopping as shopping
from db.models.product import Product as ModelProduct
from db.models.user import User as ModelUser
import api.utils.auth as auth
from api.utils.auth import oauth2_bearer

router = APIRouter()

basket = {}  # In-memory storage for simplicity

@router.post("/shop", response_model=shopping.ShopForMeResponse)
def shop_for_me(request: shopping.ShopForMeRequest, db: Session = Depends(get_db)):
    selected_items = []
    total_cost = 0
    global basket

    for category_id in request.categories:
        products = db.query(ModelProduct).filter(ModelProduct.category_id == category_id).all()
        if products:
            selected_product = choice(products)

            if selected_product.id in basket:
                basket[selected_product.id] += 1
            else:
                basket[selected_product.id] = 1

            if total_cost + selected_product.price <= request.budget:
                selected_items.append({
                    "id": selected_product.id,
                    "category_id": selected_product.category_id,
                    "name": selected_product.name,
                    "price": selected_product.price,
                    "quantity": basket[selected_product.id],
                })
                total_cost += selected_product.price
    return {"selected_items": selected_items, "total_cost": total_cost}

@router.post("/basket/add")
def add_to_basket(item: shopping.ItemInBasket, db: Session = Depends(get_db)):
    global basket

    product = db.query(ModelProduct).filter(ModelProduct.id == item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    quantity = int(item.quantity)

    if item.product_id in basket:
        basket[item.product_id] += quantity
    else:
        basket[item.product_id] = quantity
    return {"message": "Item added to basket", "basket": basket}

@router.post("/basket/remove", response_model=dict)
def remove_from_basket(item: shopping.ItemInBasket, db: Session = Depends(get_db)):
    global basket

    product = db.query(ModelProduct).filter(ModelProduct.id == item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    quantity = int(item.quantity)
    if item.product_id in basket:
        basket[item.product_id] -= quantity
        if basket[item.product_id] <= 0:
            del basket[item.product_id]
    return {"message": "Item removed from basket", "basket": basket}


@router.get("/basket", response_model=shopping.BasketResponse)
def view_basket(db: Session = Depends(get_db)):
    if not basket:
        return {"message": "Your basket is empty", "items": [], "total_cost": 0.0}

    items = []
    total_cost = 0.0

    for product_id, quantity in basket.items():
        product = db.query(ModelProduct).filter(ModelProduct.id == product_id).first()
        if product:
            subtotal = product.price * int(quantity)
            items.append({
                "product_id": product.id,
                "name": product.name,
                "price": product.price,
                "quantity": int(quantity),
                "subtotal": subtotal
            })
            total_cost += subtotal

    return {"items": items, "total_cost": total_cost}

@router.post("/checkout")
def checkout(db: Session = Depends(get_db)):
    global basket
    if not basket:
        return {"message": "Basket is empty"}

    total = 0
    for product_id, quantity in basket.items():
        product = db.query(ModelProduct).filter(ModelProduct.id == product_id).first()
        if product:
            total += product.price * quantity

    basket = {}
    return {"message": "Purchase successful", "total_paid": total}