from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, Table, Enum, Text
from sqlalchemy.orm import relationship

from db.database import Base

class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    products = relationship("Product", back_populates="category")
