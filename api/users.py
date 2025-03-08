from typing import Union, Optional, List
from fastapi import FastAPI, Path, Query, APIRouter
from pydantic import BaseModel

router = APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@router.get("/users", response_model=List[User])
async def get_users():
    return users

@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"

@router.get("/users/{user_id}")
async def get_user(user_id: int ):
    return { "user": users[user_id]}