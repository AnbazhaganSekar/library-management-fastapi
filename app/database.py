from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# ==============================
# CONFIGURATION
# ==============================

MYSQL_USER = "root"
MYSQL_PASSWORD = "2442816%40anbU"   #change this
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
DB_NAME = "library_db"

# ==============================
# STEP 1: CONNECT TO MYSQL SERVER (NO DB)
# ==============================

server_engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}",
    echo=True
)

# ==============================
# STEP 2: CREATE DATABASE IF NOT EXISTS
# ==============================

with server_engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
    conn.commit()

# ==============================
# STEP 3: CONNECT TO DATABASE
# ==============================

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{DB_NAME}"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True   # avoids stale connections
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()