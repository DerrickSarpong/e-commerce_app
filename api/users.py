from datetime import timedelta
from typing import Union, Optional, List

from fastapi import APIRouter,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.sql.annotation import Annotated

from api.utils.users import get_user, get_user_by_email, get_users, create_user
from pydantic_schema.user import UserCreate, User, UserLogin
from db.models.user import User as Model_User
from pydantic_schema.token import Token
from db.database import async_get_db, get_db
import api.utils.auth as auth

router = APIRouter()

@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.post("/users/register")
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Email is already registered"
        )
    return create_user(db=db, user=user)

@router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(Model_User).filter(Model_User.email == user_data.email).first()
    if not user or not auth.verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = auth.create_access_token(user.email, user.id)
    return {"access_token": access_token, "token_type": "bearer"}


