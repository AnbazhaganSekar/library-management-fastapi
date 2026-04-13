from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import date
from .models import Book


def get_books(db: Session):
    return db.query(Book).all()


def add_book(db: Session, data):
    try:
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
        db.refresh(book)
        return book
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def borrow_book(db: Session, book_id, user_name, user_email):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.available_copies <= 0:
        raise HTTPException(status_code=400, detail="No copies available")

    try:
        book.available_copies -= 1
        book.user_name = user_name
        book.user_email = user_email
        book.borrow_date = date.today()
        book.status = "Borrowed"

        db.commit()
        db.refresh(book)
        return book
    except:
        db.rollback()
        raise HTTPException(status_code=500, detail="Borrow failed")


def return_book(db: Session, book_id):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    try:
        book.available_copies += 1
        book.return_date = date.today()
        book.status = "Returned"

        db.commit()
        db.refresh(book)
        return book
    except:
        db.rollback()
        raise HTTPException(status_code=500, detail="Return failed")


def delete_book(db: Session, book_id):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    try:
        db.delete(book)
        db.commit()
        return {"message": "Deleted successfully"}
    except:
        db.rollback()
        raise HTTPException(status_code=500, detail="Delete failed")