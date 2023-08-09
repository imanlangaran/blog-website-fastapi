from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()



@router.get("/blog")
def home(request: Request):
    return templates.TemplateResponse("blog/home.html", {"request": request})
