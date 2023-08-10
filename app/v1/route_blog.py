from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from typing import Optional
from sqlalchemy.orm import session

from db.session import get_db
from db.repository.blog import list_blogs

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/blog")
def home(request: Request, alert: Optional[str] = None, db: session = Depends(get_db)):
    ls_blogs = list_blogs(db=db)
    return templates.TemplateResponse(
        "blog/home.html", {"request": request, "alert": alert, "blogs": ls_blogs}
    )
