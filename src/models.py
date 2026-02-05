from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional


class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str = Field(index=True)
    password: str


class UserCreate(SQLModel):
    username: str
    email: str
    password: str


class UserPublic(SQLModel):
    username: str
    email: str


class Product(SQLModel, table=True):
    __tablename__ = 'products'
    
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    price: int
    stock: int
    category_id: int = Field(index=True)
    image: str | None


class ProductCreate(SQLModel):
    name: str
    description: str
    price: int
    stock: int
    category_id: int = Field
    image: str | None
    
    
class Category(SQLModel, table=True):
    __tablename__ = 'categories'
    id: int | None = Field(index=True, primary_key=True)
    name: str = Field(unique=True, index=True)
    description: str


# class Token(BaseModel):
#     access_token: str
#     token_type: str
#
#
# class TokenData(BaseModel):
#     username: str | None = None


