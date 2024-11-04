from fastapi import APIRouter
from app.user.controller import user_router
from app.task.controller import task_router
from app.task_action_log.controller import task_action_log_router


router = APIRouter()


router.include_router(user_router, prefix="/v1/user", tags=["USER"])
router.include_router(task_router, prefix="/v1/task", tags=["TASK"])
router.include_router(task_action_log_router, prefix="/v1/task_action_log", tags=["TASK ACTION LOG"])
