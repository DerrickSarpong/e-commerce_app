from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends, HTTPException, status

from db.models.user import User
from pydantic_schema.user import  UserCreate, UserLogin
import api.utils.auth as auth

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
    return db_user

# def create_access_token(db: Session, user_data:UserLogin):
#     user = db.query(User).filter(User.email == user_data.email).first()
#     if not user or not auth.verify_password(user_data.password, user.hashed_password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials, Could not validate user")
#     access_token = auth.create_access_token({"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}
#
# def authenticate_user(email: str, password: str, db):
#     user = db.query(User).filter(User.email == email).first()
#     if not user:
#         return False
#     if not auth.pwd_context.verify(password, user.hashed_password):
#         return False
#     return user