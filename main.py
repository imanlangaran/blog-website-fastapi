from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from core.config import setting
from db.session import engine  # , Base
from db.base import Base

from app.base import router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_routes(app: FastAPI):
    app.include_router(router=router)


def config_staticfiles(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_app():
    app = FastAPI(title=setting.APP_TITLE, version=setting.APP_VERSION)
    create_tables()
    include_routes(app)
    config_staticfiles(app)
    return app


templates = Jinja2Templates(directory="templates")

app = start_app()


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("blog/home.html", {"request": request})
