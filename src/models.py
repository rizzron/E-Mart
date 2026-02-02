from sqlmodel import Field, Session, SQLModel, create_engine, select


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str = Field(index=True)
    password: str


class UserPublic(User):
    username: str
    email: str


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    price: int
    stock: int
    category_id: int = Field(index=True)
    image: str | None


class Category(SQLModel, table=True):
    id: int | None = Field(index=True, primary_key=True)
    name: str = Field(unique=True, index=True)
    description: str

