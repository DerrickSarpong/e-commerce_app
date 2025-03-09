from typing import Union, Optional, List
from fastapi import FastAPI, Path, Query, APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@router.get("/categories")
async def get_categories():
    return {"courses: []"}

