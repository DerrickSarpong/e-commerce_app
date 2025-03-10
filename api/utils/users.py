from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends, HTTPException, status

from db.models.user import User
from pydantic_schema.user import  UserCreate, UserLogin
import api.utils.auth as auth
from db.models.mixins import Timestamp

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    show = {
        "username": db_user.username,
        "email": db_user.email,
        "created_at": db_user.created_at
    }
    return {
        "message": "User registered successfully",
        **show
    }