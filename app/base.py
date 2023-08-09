from fastapi import APIRouter

from app.v1 import route_user, route_blog

router = APIRouter()

router.include_router(
    route_user.router, prefix="/auth", tags=[""], include_in_schema=False
)

router.include_router(
    route_blog.router, prefix="", tags=[""], include_in_schema=False
)
