from fastapi import APIRouter

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
def get_all_user():
    return 'All user here.'
