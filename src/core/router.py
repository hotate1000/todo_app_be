from fastapi import APIRouter
from app.user.controller import user_router
from app.task.controller import task_router


router = APIRouter()


router.include_router(user_router, prefix="/v1/user", tags=["USER"])
router.include_router(task_router, prefix="/v1/task", tags=["TASK"])
