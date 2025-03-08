from typing import Union, Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from api import users, products, categories

app = FastAPI(
    title="E-Commerce",
    description="api for e-commerce app",
    version="0.0.1",
    contact={
        "name": "Derrick Sarpong",
        "email": "derrick.sarpong.ds@gmail.com",
    },
)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(categories.router)