from sqlalchemy.orm import Session
from .models import Book
from datetime import date

def get_books(db: Session):
    return db.query(Book).all()

def add_book(db: Session, data):
    book = Book(
        book_title=data["book_title"],
        author=data["author"],
        category=data["category"],
        isbn=data["isbn"],
        total_copies=data["total_copies"],
        available_copies=data["total_copies"],
        status="Available"
    )
    db.add(book)
    db.commit()

def borrow_book(db: Session, book_id, user_name, user_email):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book and book.available_copies > 0:
        book.available_copies -= 1
        book.user_name = user_name
        book.user_email = user_email
        book.borrow_date = date.today()
        book.status = "Borrowed"
        db.commit()

def return_book(db: Session, book_id):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        book.available_copies += 1
        book.return_date = date.today()
        book.status = "Returned"
        db.commit()

def delete_book(db: Session, book_id):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()