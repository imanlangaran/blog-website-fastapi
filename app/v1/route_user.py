import json

from fastapi import APIRouter, Request, Form, Depends, responses, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic.error_wrappers import ValidationError

from db.session import get_db
from res_models.user import CreateUser
from db.repository.user import create_new_user

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})


@router.post("/register")
def register(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    errors = []
    try:
        user = CreateUser(email=email, password=password)
        create_new_user(user=user, db=db)
        return responses.RedirectResponse(
            "/blog/?alert=Successfully Registered", status_code=status.HTTP_302_FOUND
        )
    except ValidationError as e:
        ls_err = json.loads(e.json())
        for err in ls_err:
            errors.append(err.get("loc")[0] + ": " + err.get("msg"))
        return templates.TemplateResponse(
            "/auth/register.html", {"request": request, "errors": errors}
        )