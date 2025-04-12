from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from pydantic import BaseModel
# from categories import Category

class Expense(SQLModel, table=True):
    __tablename__ = "expenses"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    description: Optional[str] = Field(default=None, nullable=True)
    amount: float = Field(nullable=False)
    date: str = Field(nullable=False)

    # Relationships
    category_id: Optional[int] = Field(foreign_key="categories.id")
    category: Optional["Category"] = Relationship(back_populates="expenses")

class ExpenseCreate(BaseModel):
    name: str
    description: Optional[str] = None
    amount: float
    date: str
    category_id: Optional[int] = None

    # category: Optional["Category"] = Relationship(back_populates="expenses")

class ExpenseRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    amount: float
    date: str
    category_id: Optional[int] = None

    class Config:
        orm_mode = True