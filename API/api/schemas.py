from typing import Optional, List

from pydantic import BaseModel


class ExpenseBase(BaseModel):
    store: str
    date: str
    price: float


class Expense(ExpenseBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

