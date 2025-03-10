import pytest
from fastapi.testclient import TestClient
from main import app
from db.database import SessionLocal, engine
from db.database import Base
from api.utils.auth import create_access_token

client = TestClient(app)

Base.metadata.create_all(bind=engine)

# Sample test user credentials
test_user = {
    "username": "test_user",
    "email": "testuser@example.com",
    "password": "testpassword",
}

# Generate a test JWT token
test_token = create_access_token(email=test_user["email"], user_id =7)

# Headers with authentication token
headers = {"Authorization": f"Bearer {test_token}"}

@pytest.fixture(scope="module")
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1 Test User Registration
def test_register_user():
    response = client.post("/auth/register", json=test_user)
    assert response.status_code == 201, response.json()
    assert "message" in response.json()

    data = response.json()

    assert "username" in data
    assert "email" in data
    assert "created_at" in data

    assert data["email"] == test_user["email"]
    assert data["username"] == test_user["username"]

# 2 Test User Login
def test_login_user():
    response = client.post("/auth/login", json=test_user)
    assert response.status_code == 200
    assert "access_token" in response.json()

# 3 Test Fetch Categories
def test_get_categories():
    response = client.get("/categories", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# 4 Test Fetch Products by Category
def test_get_products_by_category():
    category_id = 1  # Assuming category ID 1 exists
    response = client.get(f"/products/{category_id}", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# 5 Test Adding Items to Basket
def test_add_to_basket():
    item = {"product_id": 54, "quantity": 2}  # Assuming product ID 1 exists
    response = client.post("/basket/add", json=item, headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Item added to basket"

# 6 Test Viewing Basket
def test_view_basket():
    response = client.get("/basket", headers=headers)
    assert response.status_code == 200
    assert "total_cost" in response.json()

# 7 Test Removing Items from Basket
def test_remove_from_basket():
    item = {"product_id": 54, "quantity": 1}
    response = client.post("/basket/remove", json=item, headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Item removed from basket"

# 8 Test Shopping Request
def test_shop_for_me():
    shop_request = {
        "categories": [1, 2],
        "budget": 100
    }
    response = client.post("/shop", json=shop_request, headers=headers)
    assert response.status_code == 200
    assert "total_cost" in response.json()

# 9 Test Checkout Process
def test_checkout():
    response = client.post("/checkout", headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Purchase successful"