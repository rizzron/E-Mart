from fastapi import APIRouter, status
from ..database import SessionDep
from ..models import Category
from typing import List
from sqlmodel import select

router = APIRouter(
    prefix='/categories',
    tags=['categories']
)


@router.get('/')
def get_all_categories(session: SessionDep) -> List[Category]:
    categories = session.get(select(Category)).all()
    return categories


