from typing import List
from models import Expense
from sqlalchemy.orm import Session
from database import SessionLocal, engine

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import schemas, crud
from models import Base

from datetime import datetime

Base.metadata.create_all(bind=engine)
api = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# origins = ["https://localhost:3000"]

# api.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials = True,
#     allow_methods = ["*"],
#     allow_headers = ["*"],
# )



@api.get("/expenses/", response_model= List[schemas.Expense])
async def show_expenses(db: Session = Depends(get_db)):
    return crud.get_expenses(db)


@api.get("/expenses/{expense_id}", response_model= schemas.Expense)
async def show_expense(expense_id: int, db: Session = Depends(get_db)):
    db_expense = crud.get_expense(db, expense_id=expense_id)
    if db_expense is None:
        raise HTTPException(status_code=404, detail="expense not found")
    return db_expense

@api.post("/expenses/", response_model= schemas.Expense)
async def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db = db, expense=expense)

@api.put("/expense/{expense_id}")
async def update_expense(expense_id: int, expense: schemas.Expense):
    return "updated"

@api.delete("/expense/{expense_id}")
async def delate_expense(expense_id: int):
    return f'deleted {expense_id}'

fake_data = {
    "store": "rona",
    "date": datetime.now(),
    "price": 20.99,
}
def  create_fake_data(db: Session):
    db_expense = Expense(**fake_data)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


if __name__== "__main__":
    database = SessionLocal()
    create_fake_data(db = database)
    print(database.query(Expense).offset(0).limit(50).all())
    # uvicorn.run(api, port=8000, host="127.0.0.1")