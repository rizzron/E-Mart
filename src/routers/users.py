from fastapi import APIRouter, status
from ..models import User, UserPublic, UserCreate
from ..database import SessionDep
from ..hashing import get_password_hash
from sqlmodel import select

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/', status_code=status.HTTP_200_OK)
def create_user(user: UserCreate, session: SessionDep):
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


@router.get('/', status_code=status.HTTP_200_OK)
def get_all_user(session: SessionDep):
    users = session.exec(select(User)).all()
    return users
