from typing import List
from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .dto import TaskActionLogDTO, TaskActionLogRequestDTO
from .service.task_action_log_service import TaskActionLogService


task_action_log_router = APIRouter()


@task_action_log_router.get(
    "",
    name="一覧取得",
    status_code=status.HTTP_200_OK,
    response_model=List[TaskActionLogDTO]
)
async def find_all(
    task_action_log_service: TaskActionLogService = Depends(TaskActionLogService.get_instance)
):
    task_action_log_dtos: List[TaskActionLogDTO] = await task_action_log_service.find_all()

    return JSONResponse(
        content=jsonable_encoder(task_action_log_dtos),
        status_code=status.HTTP_200_OK
    )


@task_action_log_router.post(
    "",
    name="作成",
    status_code=status.HTTP_201_CREATED,
    response_model=TaskActionLogDTO
)
async def save(
    params: TaskActionLogRequestDTO,
    task_action_log_service: TaskActionLogService = Depends(TaskActionLogService.get_instance)
):
    task_action_log_dto: TaskActionLogDTO = await task_action_log_service.save(params=params)

    return JSONResponse(
        content=jsonable_encoder(task_action_log_dto),
        status_code=status.HTTP_201_CREATED
    )
