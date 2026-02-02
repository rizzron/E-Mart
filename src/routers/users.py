from fastapi import APIRouter, status
from ..models import User
from ..schemas import UserPublic, UserCreate
from ..database import SessionDep

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/', status_code=status.HTTP_200_OK)
def create_user(user: UserCreate, session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
