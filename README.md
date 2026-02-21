# E-Mart

E-Mart is a secure and scalable RESTful E-Commerce API built with FastAPI.
It provides structured backend services for managing products and categories with filtering, pagination, and relational data handling.

The project focuses on clean architecture, modular code design, and proper API documentation using Swagger (OpenAPI).

# 🚀 Features

Product Management (Create, Read, Update, Delete)

Category Management (Create, Read, Update, Delete)

Retrieve products by category

Filtering by price range

Pagination support

Relational data handling (Product ↔ Category)

Input validation using Pydantic

Interactive API documentation using Swagger UI

Clean and modular project structure

# 🛠 Tech Stack

Framework: FastAPI

ORM: SQLModel

Database: SQLite

API Documentation: Swagger (OpenAPI)

Language: Python

# 📌 API Documentation

The API is fully documented using Swagger UI.

Once the server is running, you can access:

http://127.0.0.1:8000/docs

Below are screenshots of the interactive Swagger API documentation:

<img width="1103" height="656" alt="Screenshot 2026-02-22 at 2 27 09 AM" src="https://github.com/user-attachments/assets/e405a8dc-7ea5-4158-beb3-ebfad567a132" />

# ▶️ How to Run the Project

Clone the repository

Create a virtual environment

Install dependencies

pip install -r requirements.txt

Run the server

uvicorn main:app --reload
🎯 Project Objective

# This project was built to strengthen backend development skills including:

RESTful API design

Database schema design and relationships

Filtering and pagination implementation

Clean architecture and modular code practices

API documentation standards
