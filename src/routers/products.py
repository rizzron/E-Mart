from fastapi import APIRouter, status, HTTPException
from sqlmodel import select
from ..models import Product, ProductCreate
from ..database import SessionDep

router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.get('/', status_code=status.HTTP_200_OK)
def get_all_products(session: SessionDep, category_id: int = None, min_price: int | None = None, max_price: int | None = None):
    products = session.exec(select(Product)).all()
    return products


@router.post('/', status_code=status.HTTP_200_OK)
def create(product: ProductCreate, session: SessionDep):
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
