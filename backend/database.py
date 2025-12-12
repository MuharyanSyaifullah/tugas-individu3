# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

# Mengambil URL database dari .env, default ke SQLite jika tidak ada
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./feedback.db")

# Argumen khusus untuk SQLite agar tidak error di thread berbeda
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()