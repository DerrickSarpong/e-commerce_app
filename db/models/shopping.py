from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, Table, Enum, Text
from sqlalchemy.orm import relationship

from db.database import Base
from .mixins import Timestamp

class ShoppingRequest(Timestamp,Base):
    __tablename__ = "shopping_requests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    budget = Column(Float, nullable=False)
    user = relationship("User")