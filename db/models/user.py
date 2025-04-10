from sqlalchemy import Column, Integer, String

from ..database import Base
from .mixins import Timestamp

class User(Timestamp,Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True,  nullable=False )
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String)
