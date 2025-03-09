from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    category_id: int

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True