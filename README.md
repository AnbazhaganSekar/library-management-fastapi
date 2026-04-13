# 📚 Library Management System

A backend-driven web application for managing library inventory, borrowing workflows, and book availability. Built using **FastAPI**, **MySQL**, and **SQLAlchemy**, with a lightweight HTML interface for interaction.

---

## 📌 Overview

This project demonstrates a **CRUD-based service architecture** with server-side rendering, focusing on:

* Inventory lifecycle management
* Borrow/return workflows
* Database-driven state tracking
* Clean separation of API, business logic, and persistence layers

---

## 🚀 Features

* Create and manage book records
* Track total and available copies
* Borrow and return books with user details
* Delete records from inventory
* Real-time availability updates

---

## 🧱 Tech Stack

| Layer       | Technology |
| ----------- | ---------- |
| Backend API | FastAPI    |
| ORM         | SQLAlchemy |
| Database    | MySQL      |
| Frontend    | HTML, CSS  |
| Server      | Uvicorn    |

---

## 🏗️ System Architecture

The application follows a **layered architecture pattern**:

* **API Layer (`main.py`)**
  Handles HTTP requests, routing, and dependency injection

* **Service Layer (`crud.py`)**
  Encapsulates business logic and database operations

* **Data Layer (`models.py`)**
  Defines ORM models and schema mappings

* **Infrastructure Layer (`database.py`)**
  Manages database connections and session lifecycle

---

## 📂 Project Structure

```id="y9yd39"
library_project/
│
├── app/
│   ├── main.py        # API routes
│   ├── database.py    # DB connection
│   ├── models.py      # ORM models
│   ├── crud.py        # Business logic
│
├── templates/         # HTML templates
├── static/            # CSS files
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash id="l1o6wf"
git clone https://github.com/AnbazhaganSekar/library-management-fastapi.git
cd library-management-fastapi
```

### 2. Create Virtual Environment

```bash id="3f1s4p"
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash id="t3h2v7"
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env id="hsl1u8"
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
DB_NAME=library_db
```

> ⚠️ Do not commit `.env` files. Use environment variables for all sensitive configuration.

---

### 5. Run the Application

```bash id="6z9d0y"
uvicorn app.main:app --reload
```

---

### 6. Access the Application

* Web Interface: http://127.0.0.1:8000
* Interactive API Docs (Swagger): http://127.0.0.1:8000/docs

---

## 🗄️ Database Design

### Table: `books`

| Column           | Description       |
| ---------------- | ----------------- |
| id               | Primary key       |
| book_title       | Title of the book |
| author           | Author name       |
| category         | Book category     |
| isbn             | Unique identifier |
| total_copies     | Total stock       |
| available_copies | Available stock   |
| user_name        | Borrower name     |
| user_email       | Borrower email    |
| borrow_date      | Borrow timestamp  |
| return_date      | Return timestamp  |
| status           | Current status    |

---

## 📡 API Endpoints

| Method | Endpoint       | Description        |
| ------ | -------------- | ------------------ |
| GET    | `/`            | Retrieve all books |
| POST   | `/add`         | Add a new book     |
| POST   | `/borrow/{id}` | Borrow a book      |
| POST   | `/return/{id}` | Return a book      |
| GET    | `/delete/{id}` | Delete a book      |

---

## ⚠️ Known Limitations

* No authentication or authorization layer
* Borrowing is not normalized (single user overwrite model)
* No input validation via Pydantic schemas
* No pagination or filtering
* No concurrency control for stock updates

---

## 🔐 Security Considerations

* Credentials are managed via environment variables
* SQLAlchemy ORM mitigates raw SQL injection risks
* Recommended enhancements:

  * JWT-based authentication
  * Role-based access control (RBAC)
  * Rate limiting and request validation
  * HTTPS deployment behind reverse proxy

---

## 🚀 Roadmap / Enhancements

* Implement JWT authentication and user roles
* Introduce borrow history table (normalized schema)
* Add Pydantic validation models
* Containerize using Docker
* CI/CD pipeline using GitHub Actions
* Observability (logging, monitoring)

---

## 👨‍💻 Author

**Anbazhagan S**
