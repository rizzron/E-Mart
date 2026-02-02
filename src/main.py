from fastapi import FastAPI
from routers import users, products, categories
import database
import models

app = FastAPI()

database.create_db_and_tables()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(categories.router)
