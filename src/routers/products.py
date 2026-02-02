from fastapi import APIRouter

router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.get('/')
def get_all_products():
    return 'List of all products'
