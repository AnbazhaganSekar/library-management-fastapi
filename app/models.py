from sqlalchemy import Column, Integer, String, Date
from .database import Base


class Book(Base):


    id = Column(Integer, primary_key=True, index=True)
    book_title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    category = Column(String(100))
    isbn = Column(String(50), unique=True, index=True)
    total_copies = Column(Integer, nullable=False)
    available_copies = Column(Integer, nullable=False)

    user_name = Column(String(100))
    user_email = Column(String(100), index=True)

    borrow_date = Column(Date)
    return_date = Column(Date)

    status = Column(String(50), default="Available")
