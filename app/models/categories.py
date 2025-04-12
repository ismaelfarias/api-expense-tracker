from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from pydantic import BaseModel
# from expenses import Expense
# from incomes import Income

class Category(SQLModel, table=True):
    __tablename__ = "categories"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    description: Optional[str] = Field(default=None, nullable=True)

    # Relationships
    expenses: list["Expense"] = Relationship(back_populates="category")
    incomes: list["Income"] = Relationship(back_populates="category")

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True