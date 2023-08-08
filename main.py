from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from core.config import setting
from db.session import engine  # , Base
from db.base import Base

from app.base import router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_routes(app: FastAPI):
    app.include_router(router=router)


def start_app():
    app = FastAPI(title=setting.APP_TITLE, version=setting.APP_VERSION)
    create_tables()
    include_routes(app)
    return app

templates = Jinja2Templates(directory="templates")

app = start_app()



@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("blog/home.html", {"request":request})
