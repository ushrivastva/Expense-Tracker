from fastapi import FastAPI, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import date

import crud, schemas, models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
template = Jinja2Templates(directory="template")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_expenses(request: Request, db: Session = Depends(get_db)):
    expenses = crud.get_expenses(db)
    return template.TemplateResponse(request, "index.html", {"expenses": expenses})
@app.post("/add")
def add_expense(
    title: str = Form(...),
    amount: float = Form(...),
    category: str = Form(...),
    expense_date: date = Form(...),
    db: Session = Depends(get_db)
):

    expense = schemas.ExpenseCreate(title=title, amount=amount, category=category, date=expense_date)
    crud.create_expense(db, expense)

    return RedirectResponse(url="/", status_code=303)

@app.post("/delete/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    crud.delete_expense(db, expense_id)
    return RedirectResponse(url="/", status_code=303)