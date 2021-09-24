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

def delete_expense(db: Session, expense_id: int):
    item = db.query(Expense).filter(Expense.id == expense_id).first()
    db.delete(item)
    db.commit()

def update_expense(db: Session, expense_id: int, expense: ExpenseCreate):
    item = db.query(Expense).filter(Expense.id == expense_id).first()
    item.store = expense.store
    item.date = expense.date
    item.price = expense.price
    db.commit()
    db.refresh(item)