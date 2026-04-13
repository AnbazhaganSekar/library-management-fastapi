# 📚 Library Management System

A full-stack web application built using **FastAPI, MySQL, HTML, and CSS** to manage books, borrowing, and returns.

---

## 🚀 Features

* Add new books
* View all books
* Borrow books
* Return books
* Delete books
* Track availability and status

---

## 🛠️ Tech Stack

* Backend: FastAPI
* Database: MySQL
* Frontend: HTML, CSS
* ORM: SQLAlchemy

---

## 📂 Project Structure

```
library_project/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/AnbazhaganSekar/library-management-fastapi.git
cd library-management-fastapi
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Run Application

```
uvicorn app.main:app --reload
```

---

### 5. Open in Browser

```
http://127.0.0.1:8000
```

---

## 🗄️ Database

* MySQL database: `library_db`
* Tables are created automatically using SQLAlchemy

---

## 📬 API Endpoints

| Method | Endpoint       | Description    |
| ------ | -------------- | -------------- |
| GET    | `/`            | View all books |
| POST   | `/add`         | Add new book   |
| POST   | `/borrow/{id}` | Borrow book    |
| POST   | `/return/{id}` | Return book    |
| GET    | `/delete/{id}` | Delete book    |

---

## 📌 Sample Data

Includes:

* Available books
* Borrowed books
* Returned books

---

## 👨‍💻 Author

Anbazhagan S
