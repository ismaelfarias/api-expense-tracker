from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.categories import Category
from app.database.engine import get_session

router = APIRouter()

@router.get("/categories/", response_model=list[Category])
async def get_categories(session: Session = Depends(get_session)):
    categories = session.exec(select(Category)).all()
    return categories

@router.get("/categories/{category_id}", response_model=Category)
async def get_category(category_id: int, session: Session = Depends(get_session)):
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/categories/", response_model=Category)
async def create_category(category: Category, session: Session = Depends(get_session)):
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

@router.put("/categories/{category_id}", response_model=Category)
async def update_category(category_id: int, category: Category, session: Session = Depends(get_session)):
    db_category = session.get(Category, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db_category.name = category.name
    db_category.description = category.description
    session.commit()
    session.refresh(db_category)
    return db_category

@router.delete("/categories/{category_id}", response_model=Category)
async def delete_category(category_id: int, session: Session = Depends(get_session)):
    db_category = session.get(Category, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    session.delete(db_category)
    session.commit()
    return db_category