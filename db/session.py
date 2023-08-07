# create_engine
# session_maker

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


####################################################################
# from sqlalchemy.orm import declarative_base

# Base = declarative_base()