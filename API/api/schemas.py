from typing import Optional, List

from pydantic import BaseModel

from datetime import datetime


class ExpenseBase(BaseModel):
    store: str
    date: datetime
    price: float


class Expense(ExpenseBase):
    id: int
    # owner_id: int

    class Config:
        orm_mode = True


class ExpenseCreate(ExpenseBase):
    pass



