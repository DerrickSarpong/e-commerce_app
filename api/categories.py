from typing import Union, Optional, List
from fastapi import FastAPI, Path, Query, APIRouter
from pydantic import BaseModel

router = APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@router.get("/categories/")
async def get_categories():
    return {"courses: []"}

@router.post("/categories")
async def create_categories(user: User):
    return {"courses: []"}

@router.get("/{category}/{id}")
async def get_categories():
    return {"courses: []"}

@router.patch("/{category}/{id}")
async def get_categories():
    return {"courses: []"}

@router.delete("/{category}/{id}")
async def get_categories():
    return {"courses: []"}
