from sqlalchemy.orm import Session
from models import  Expense
from schemas import ExpenseCreate

def get_expenses(db: Session):
    return db.query(Expense).all()

def get_expense(db: Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()

def create_expense(db: Session, expense: ExpenseCreate):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def update_expense(db: Session, expense_id: int, expense: ExpenseCreate):
    db_expense = get_expense(db, expense_id)
    if db_expense:
        for key, value in expense.dict().items():
            setattr(db_expense, key, value)
        db.commit()
        db.refresh(db_expense)
    return db_expense

def delete_expense(db: Session, expense_id: int):
    db_expense = get_expense(db, expense_id)
    if db_expense:
        db.delete(db_expense)
        db.commit()
    return db_expense