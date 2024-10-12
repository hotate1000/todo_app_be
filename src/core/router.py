from fastapi import APIRouter
from app.user.controller import user_router


router = APIRouter()


router.include_router(user_router, prefix="/v1/user", tags=["USER"])
