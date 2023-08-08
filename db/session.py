# create_engine
# session_maker
# Generator -> typing

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


####################################################################
# from sqlalchemy.orm import declarative_base

# Base = declarative_base()