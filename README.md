
A full-stack product management application built with FastAPI and React, featuring complete CRUD operations for managing product inventory.

🚀 Features
RESTful API - Built with FastAPI for high performance

CRUD Operations - Create, Read, Update, and Delete products

Database Integration - SQLAlchemy ORM with structured models

Modern Frontend - React-based user interface

Product Management - Track product name, quantity, description, and price

📋 Tech Stack
Backend
FastAPI - Modern, fast web framework for building APIs

SQLAlchemy - SQL toolkit and ORM

Pydantic - Data validation using Python type annotations

Python 3.11

Frontend
React (v18.2.0)

Axios (v1.7.3) - HTTP client

React-DOM (v18.2.0)

React-Scripts (v5.0.1)

📁 Project Structure
text
FastTel/
├── frontend/           # React frontend application
│   ├── public/        # Static files
│   ├── src/           # Source files
│   ├── package.json   # Frontend dependencies
│   └── package-lock.json
├── main.py            # FastAPI application entry point
├── models.py          # Pydantic models
├── database_model.py  # SQLAlchemy database models
├── databse.py         # Database connection configuration
├── config.py          # Application configuration
├── practice.py        # Practice/testing file
└── .gitignore
🛠️ Installation
Backend Setup
Clone the repository

bash
git clone https://github.com/roshankumbharx/FastTel.git
cd FastTel
Create a virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install fastapi uvicorn sqlalchemy pydantic pydantic-settings
Configure environment variables
Create a .env file in the root directory with your database configuration

Run the FastAPI server

bash
uvicorn main:app --reload
The API will be available at http://localhost:8000

Frontend Setup
Navigate to the frontend directory

bash
cd frontend
Install dependencies

bash
npm install
Start the development server

bash
npm start
The frontend will be available at http://localhost:3000

📡 API Endpoints
Method	Endpoint	Description
GET	/products	Get all products
GET	/products/{id}	Get a specific product by ID
POST	/products	Create a new product
PUT	/products/{id}	Update an existing product
DELETE	/products/{id}	Delete a product by ID
📊 Data Model
Product Schema
python
{
    "id": int,
    "name": str,
    "quantity": int,
    "description": str,
    "price": float
}
🔧 Configuration
The application uses pydantic-settings for configuration management. Database connection details are stored in the .env file:

text
db_url=your_database_url_here
📝 API Documentation
Once the server is running, you can access:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc