from fastapi import FastAPI

from api import users, products, categories
from db.database import engine
from db.models import user, category, product

user.Base.metadata.create_all(bind=engine)
category.Base.metadata.create_all(bind=engine)
product.Base.metadata.create_all(bind=engine)


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

@app.get("/")
def root():
    return {"message": "Welcome to Shop for Me API!"}