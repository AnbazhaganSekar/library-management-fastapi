from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import crud

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    books = crud.get_books(db)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "books": books
    })


@app.post("/add")
def add_book(
    book_title: str = Form(...),
    author: str = Form(...),
    category: str = Form(...),
    isbn: str = Form(...),
    total_copies: int = Form(...),
    db: Session = Depends(get_db)
):
    crud.add_book(db, {
        "book_title": book_title,
        "author": author,
        "category": category,
        "isbn": isbn,
        "total_copies": total_copies
    })
    return {"message": "Book Added"}


@app.post("/borrow/{book_id}")
def borrow_book(
    book_id: int,
    user_name: str = Form(...),
    user_email: str = Form(...),
    db: Session = Depends(get_db)
):
    crud.borrow_book(db, book_id, user_name, user_email)
    return {"message": "Borrowed"}


@app.post("/return/{book_id}")
def return_book(book_id: int, db: Session = Depends(get_db)):
    crud.return_book(db, book_id)
    return {"message": "Returned"}


@app.get("/delete/{book_id}")
def delete(book_id: int, db: Session = Depends(get_db)):
    crud.delete_book(db, book_id)
    return {"message": "Deleted"}
