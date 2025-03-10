# E-Commerce Backend with FastAPI

## 📌 Project Overview
This is a simple e-commerce backend built with **FastAPI** that allows users to:
- Register and authenticate using **JWT tokens**.
- Browse categories and products.
- Request a shopper to pick items within a budget.
- Manage a shopping basket.
- Simulate a checkout process.

## 🛠️ Technologies Used
- **FastAPI** (Backend Framework)
- **PostgreSQL** (Database)
- **SQLAlchemy** (ORM)
- **Pydantic** (Data validation)
- **JWT** (Authentication)

## 🚀 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/DerrickSarpong/e-commerce_app.git
cd ecommerce-fastapi
```

### **2️⃣ Set Up a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up the Database**
Ensure PostgreSQL is installed and running. Update your `.env` file with your database credentials:
```ini
DATABASE_URL=postgresql://username:password@localhost:5432/ecommerce_db
```
Then, run the migrations:
```sh
alembic upgrade head
```

### **5️⃣ Populate the Database**
Run the script to add default categories and products:
```sh
python populate_db.py
```

### **6️⃣ Start the FastAPI Server**
```sh
uvicorn main:app --reload
```

## 📖 API Endpoints
### **🟢 Authentication**
| Method | Endpoint        | Description         |
|--------|---------------|--------------------|
| POST   | `/auth/register` | Register a new user |
| POST   | `/auth/login` | Log in and receive JWT |

### **🛍️ Category & Product Management**
| Method | Endpoint        | Description         |
|--------|---------------|--------------------|
| GET   | `/categories` | Get all categories |
| GET   | `/products/{category_id}` | Get products by category |

### **🛒 Shopping Basket**
| Method | Endpoint         | Description         |
|--------|------------------|--------------------|
| POST   | `/shop    `       | Get products by category |
| POST   | `/basket/add`    | Add item to basket |
| POST   | `/basket/remove` | Remove item from basket |
| GET    | `/basket`        | View current basket |

### **💰 Checkout & Payment Simulation**
| Method | Endpoint        | Description         |
|--------|---------------|--------------------|
| POST   | `/checkout` | Simulate checkout and payment |

## 📘 API Documentation
FastAPI provides automatic API documentation:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🧪 Running Tests
To run unit tests:
```sh
pytest
```

## ✨ Contributing
Feel free to submit a pull request or open an issue for improvements.

## 📜 License
This project is licensed under the MIT License.

---
**Enjoy Coding! 🚀**

