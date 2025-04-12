from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from pydantic import BaseModel
from datetime import datetime
# from categories import Category

class Income(SQLModel, table=True):
    __tablename__ = "incomes"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    description: Optional[str] = Field(default=None, nullable=True)
    amount: float = Field(nullable=False)
    date: str = Field(nullable=False)

    # Relationships
    category_id: Optional[int] = Field(foreign_key="categories.id")
    category: Optional["Category"] = Relationship(back_populates="incomes")

class IncomeCreate(BaseModel):
    name: str
    description: Optional[str] = None
    amount: float
    date: datetime
    category_id: Optional[int] = None
    # category: Optional["Category"] = Relationship(back_populates="incomes")

class IncomeRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    amount: float
    date: datetime
    category_id: Optional[int] = None

    class Config:
        orm_mode = True