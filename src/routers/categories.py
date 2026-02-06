from fastapi import APIRouter, status, HTTPException
from ..database import SessionDep
from ..models import Category, CategoryCreate
from typing import List
from sqlmodel import select

router = APIRouter(
    prefix='/categories',
    tags=['categories']
)


@router.get('/')
def get_all_categories(session: SessionDep) -> List[Category]:
    categories = session.exec(select(Category)).all()
    return categories


@router.get('/{category_id', status_code=status.HTTP_200_OK)
def get_by_id(category_id: int, session: SessionDep) -> Category:
    category = session.get(Category, category_id)
    return category


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, session: SessionDep):
    new_category = Category(name=category.name, description=category.description)
    session.add(new_category)
    session.commit()
    session.refresh(new_category)
    return new_category


@router.put('/{category_id}', status_code=status.HTTP_202_ACCEPTED)
def update_by_id(category_id: int, category: CategoryCreate, session: SessionDep):
    db_category = session.get(Category, category_id)

    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No category found with the {category_id}')

    update_data = category.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_category, key, value)

    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return category


@router.delete('/{category_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(category_id: int, session: SessionDep):
    category = session.get(Category, category_id)
    
    session.delete(category)
    session.commit()
    return f'The category with the {category_id} has been deleted.'
