from fastapi import FastAPI
from db.session import engine #, Base
from db.base import Base

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_app():
    app = FastAPI()
    create_tables()
    return app

app = start_app()


@app.get("/")
def home():
    return {"msg": "first function..."}
