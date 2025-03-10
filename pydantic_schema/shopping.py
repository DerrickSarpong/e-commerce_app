from pydantic import BaseModel, ConfigDict
from typing import List
from pydantic_schema.product import ProductResponse
from datetime import datetime

# ✅ Shopping Request Schema ("Shop for Me")
class ShopForMeRequest(BaseModel):
    budget: float
    categories: List[int]  # List of category IDs


class ShopForMeResponse(BaseModel):
    selected_items: List[ProductResponse]
    total_cost: float

class SelectedItem(BaseModel):
    id: int
    product_id: int
    name: str
    category_id: int
    price: float

# ✅ Basket Management Schemas
class BasketItem(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int
    subtotal: float

class ItemInBasket(BaseModel):
    product_id: int
    quantity: int

class BasketResponse(BaseModel):
    items: List[BasketItem]
    total_cost: float

class ShoppingRequestBase(BaseModel):
    budget: float

class ShoppingRequestCreate(ShoppingRequestBase):
    pass

class ShoppingRequestResponse(ShoppingRequestBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)