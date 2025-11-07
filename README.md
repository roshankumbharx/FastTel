# FastTel — Full-Stack Product Management Application

A full-stack **Product Management System** built using **FastAPI** and **React**, supporting complete **CRUD** functionality to manage product inventory efficiently.

## 🚀 Features

- **RESTful API** built with **FastAPI** for high performance  
- **CRUD Operations** — Create, Read, Update, and Delete products  
- **Database Integration** using **SQLAlchemy ORM**  
- **Modern Frontend** built with **React**  
- Manage product **name, quantity, description, and price**  

## 🧰 Tech Stack

### Backend
| Tool | Purpose |
|------|---------|
| FastAPI | Backend API framework |
| SQLAlchemy | ORM & database interaction |
| Pydantic | Data validation |
| Python 3.11 | Programming language |

### Frontend
| Tool | Purpose |
|------|---------|
| React (v18.2.0) | UI framework |
| Axios (v1.7.3) | HTTP client |
| React-DOM (v18.2.0) | DOM rendering |
| React-Scripts (v5.0.1) | Development tooling |

## 📁 Project Structure

```
FastTel/
├── frontend/              # React frontend
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── package-lock.json
├── main.py                # FastAPI entry point
├── models.py              # Pydantic models
├── database_model.py      # SQLAlchemy models
├── databse.py             # Database configuration
├── config.py              # App configuration
├── practice.py            # Test / practice logic
└── .gitignore
```

## 🛠️ Installation & Setup

### Backend Setup

```bash
git clone https://github.com/roshankumbharx/FastTel.git
cd FastTel
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic pydantic-settings
```

Create **.env** file:

```
db_url=your_database_url_here
```

Run the server:

```bash
uvicorn main:app --reload
```

> API will run at: **http://localhost:8000**

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

> Frontend available at: **http://localhost:3000**

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products` | Get all products |
| GET | `/products/{id}` | Get product by ID |
| POST | `/products` | Create new product |
| PUT | `/products/{id}` | Update existing product |
| DELETE | `/products/{id}` | Delete product |

## 📊 Product Data Model

```json
{
  "id": 1,
  "name": "Laptop",
  "quantity": 5,
  "description": "A powerful device",
  "price": 55000.00
}
```

## 📝 API Documentation

| Tool | URL |
|------|-----|
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

