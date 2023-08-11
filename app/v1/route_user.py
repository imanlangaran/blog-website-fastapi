import json

from fastapi import APIRouter, Request, Form, Depends, responses, status, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic.error_wrappers import ValidationError

from db.session import get_db
from res_models.user import CreateUser
from db.repository.user import create_new_user
from core.security import create_access_token
from apis.v1.route_login import authenticate_user

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


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("/auth/login.html", {"request": request})


@router.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    errors = []
    user = authenticate_user(email=email, password=password, db=db)
    if not user:
        errors.append("Incorrect emain or password")
        return templates.TemplateResponse(
            "auth/login.html", {"request": request, "errors": errors}
        )
    access_token = create_access_token(data={"sub": email})
    response = responses.RedirectResponse(
        "/blog?alert=Successfully Logged In", status_code=status.HTTP_302_FOUND
    )
    response.set_cookie(
        key="access_token", value=f"Bearer {access_token}", httponly=True
    )
    return response


# def get_current_user()