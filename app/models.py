from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index= True)
    title = Column(String, index=True)
    amount = Column(Float)
    category = Column(String)
    date = Column(Date)