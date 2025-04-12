from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.expenses import Expense
from app.database.engine import get_session
from datetime import datetime

router = APIRouter()

@router.get("/expenses/", response_model=list[Expense])
async def get_expenses(session: Session = Depends(get_session)):
    expenses = session.exec(select(Expense)).all()
    return expenses 

@router.post("/expenses/", response_model=Expense)
async def create_expense(expense: Expense, session: Session = Depends(get_session)):
    if not expense.date:
        expense.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    session.add(expense)
    session.commit()
    session.refresh(expense)
    return expense

@router.get("/expenses/{expense_id}", response_model=Expense)
async def get_expense(expense_id: int, session: Session = Depends(get_session)):    
    expense = session.get(Expense, expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.get("/expenses/category/{category_id}", response_model=list[Expense])
async def get_expenses_by_category(category_id: int, session: Session = Depends(get_session)):
    expenses = session.exec(select(Expense).where(Expense.category_id == category_id)).all()
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found for this category")
    return expenses

@router.put("/expenses/{expense_id}", response_model=Expense)
async def update_expense(expense_id: int, expense: Expense, session: Session = Depends(get_session)):
    db_expense = session.get(Expense, expense_id)
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db_expense.name = expense.name
    db_expense.amount = expense.amount
    db_expense.category_id = expense.category_id
    session.commit()
    session.refresh(db_expense)
    return db_expense

@router.delete("/expenses/{expense_id}", response_model=Expense)
async def delete_expense(expense_id: int, session: Session = Depends(get_session)):
    db_expense = session.get(Expense, expense_id)
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    session.delete(db_expense)
    session.commit()
    return db_expense