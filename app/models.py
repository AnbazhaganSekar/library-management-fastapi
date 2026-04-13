from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    book_title = Column(String(255))
    author = Column(String(255))
    category = Column(String(100))
    isbn = Column(String(50))
    total_copies = Column(Integer)
    available_copies = Column(Integer)
    user_name = Column(String(100))
    user_email = Column(String(100))
    borrow_date = Column(Date)
    return_date = Column(Date)
    status = Column(String(50))