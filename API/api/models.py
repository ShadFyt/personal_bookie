from sqlalchemy import Boolean, Column, ForeignKey, Float, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index= True)
    email = Column(String, unique= True, index= True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default= True)

    expenses = relationship("Expense", back_populates="owner")


class Expense(Base):
    __tablename__: "expenses"

    id = Column(Integer, primary_key= True, index= True)
    date = Column(DateTime, default = (datetime.now))
    store = Column(String, nullable= True)
    price = Column(Float)

    owner = relationship("User", back_populates="expenses")
