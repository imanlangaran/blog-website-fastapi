from sqlalchemy.orm import Session
from typing import Optional
from datetime import timedelta, datetime
from jose import jwt

from db.repository.user import get_user
from core.hashing import Hasher
from core.config import setting


def authenticate_user(email: str, password: str, db: Session):
    user = get_user(email=email, db=db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expire_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.now() + expire_delta
    else:
        expire = datetime.now() + timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, key=setting.SECRET_KEY, algorithm=setting.ALGORITHM)
