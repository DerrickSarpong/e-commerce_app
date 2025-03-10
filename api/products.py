from typing import List

from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import async_get_db, get_db, Base
from pydantic_schema.product import ProductBase, Product
from db.models.product import Product as ModelProduct

router = APIRouter()

@router.post("/products/{category_id}", response_model=List[ProductBase])
async def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    products = db.query(ModelProduct).filter(ModelProduct.category_id == category_id).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found in this category")
    return products
