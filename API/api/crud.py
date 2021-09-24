from sqlalchemy.orm import Session

from models import Expense
from schemas import ExpenseCreate


def get_expenses(db: Session):
    return db.query(Expense).all()

def get_expense(db: Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()

def create_expense(db: Session, expense: ExpenseCreate):
    db_expense = Expense(
        store = expense.store,
        date = expense.date, 
        price = expense.price
    )
    print("created!!!!!")
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense
