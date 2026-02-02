from fastapi import APIRouter

router = APIRouter(
    prefix='/categories',
    tags=['categories']
)


@router.get('/')
def get_all_categories():
    return 'All categories here'
