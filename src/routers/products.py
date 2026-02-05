from fastapi import APIRouter, status, HTTPException, Query
from sqlmodel import select
from ..models import Product, ProductCreate
from ..database import SessionDep
from typing import Annotated

router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.get('/', status_code=status.HTTP_200_OK)
def get_all_products(
        session: SessionDep,
        category_id: int | None = None,
        min_price: int | None = None,
        max_price: int | None = None,
        page: int = Query(1, ge=1),
        limit: int = Query(10, le=100, ge=1)
):
    query = select(Product)

    if category_id is not None:
        query = query.where(Product.category_id == category_id)

    if min_price is not None:
        query = query.where(Product.price >= min_price)

    if max_price is not None:
        query = query.where(Product.price <= max_price)

    offset = (page - 1) * limit

    query = query.offset(offset).limit(limit)

    products = session.exec(query).all()

    return products


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, session: SessionDep):
    new_product = Product(name=product.name, description=product.description, price=product.price,
                          stock=product.stock, category_id=product.category_id, image=product.image)
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product


@router.get('/{product_id}', status_code=status.HTTP_200_OK)
def get_by_id(product_id, session: SessionDep):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No product found with the ID {product_id}')
    return product


@router.put('/{product_id}', status_code=status.HTTP_202_ACCEPTED)
def update_by_id(product_id: int, product: ProductCreate, session: SessionDep):
    db_product = session.get(Product, product_id)

    if not db_product:
        raise HTTPException(status_code=404, detail=f'No product found with the ID {product_id}')

    update_data = product.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)

    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(product_id: int, session: SessionDep):
    product = session.get(Product, product_id)

    if not product:
        raise HTTPException(status_code=404, detail=f'No product found with the ID {product_id}')

    session.delete(product)
    session.commit()
    return f'The product with the ID of {product_id} has been deleted.'
