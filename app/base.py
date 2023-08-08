from fastapi import APIRouter

from app.v1 import route_user

router = APIRouter()

router.include_router(
    route_user.router, prefix="/auth", tags=[""], include_in_schema=False
)
