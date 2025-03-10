from typing import List

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from db.models.category import Category as Model_Category
from pydantic_schema.category import CategoryResponse
from db.database import async_get_db, get_db

router = APIRouter()

@router.get("/categories", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Model_Category).all()

