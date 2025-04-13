from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.incomes import Income, IncomeCreate, IncomeRead
from app.database.engine import get_session
from datetime import datetime

router = APIRouter()

@router.get("/incomes/", response_model=list[Income])
async def get_incomes(session: Session = Depends(get_session)):
    incomes = session.exec(select(Income)).all()
    return incomes

@router.get("/incomes/{income_id}", response_model=IncomeRead)
async def get_income(income_id: int, session: Session = Depends(get_session)):    
    income = session.get(Income, income_id)
    if not income:
        raise HTTPException(status_code=404, detail="Income not found")
    return income

@router.get("/incomes/category/{category_id}", response_model=list[Income])
async def get_incomes_by_category(category_id: int, session: Session = Depends(get_session)):
    incomes = session.exec(select(Income).where(Income.category_id == category_id)).all()
    if not incomes:
        raise HTTPException(status_code=404, detail="No incomes found for this category")
    return incomes

@router.post("/incomes/", response_model=IncomeRead)
async def create_income(income: Income, session: Session = Depends(get_session)):
    if not income.date:
        income.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    session.add(income)
    session.commit()
    session.refresh(income)
    return income

@router.put("/incomes/{income_id}", response_model=Income)
async def update_income(income_id: int, income: Income, session: Session = Depends(get_session)):
    db_income = session.get(Income, income_id)
    if not db_income:
        raise HTTPException(status_code=404, detail="Income not found")
    db_income.name = income.name
    db_income.amount = income.amount
    db_income.category_id = income.category_id
    session.commit()
    session.refresh(db_income)
    return db_income

@router.delete("/incomes/{income_id}", response_model=IncomeCreate)
async def delete_income(income_id: int, session: Session = Depends(get_session)):
    db_income = session.get(Income, income_id)
    if not db_income:
        raise HTTPException(status_code=404, detail="Income not found")
    session.delete(db_income)
    session.commit()
    return db_income