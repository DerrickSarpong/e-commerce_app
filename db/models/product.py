from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, Table, Enum, Text
from sqlalchemy.orm import relationship

from db.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")