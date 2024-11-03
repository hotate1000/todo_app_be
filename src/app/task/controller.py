from typing import List
from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .dto import TaskDTO, TaskRequestDTO
from .service.task_service import TaskService

task_router = APIRouter()


@task_router.get(
    "",
    name="一覧取得",
    status_code=status.HTTP_200_OK,
    response_model=List[TaskDTO]
)
async def find_all(
    task_service: TaskService = Depends(TaskService.get_instance)
):
    task_dtos: List[TaskDTO] = await task_service.find_all()

    return JSONResponse(
        content=jsonable_encoder(task_dtos),
        status_code=status.HTTP_200_OK
    )


@task_router.post(
    "",
    name="作成",
    status_code=status.HTTP_201_CREATED,
    response_model=TaskDTO
)
async def save(
    params: TaskRequestDTO,
    task_service: TaskService = Depends(TaskService.get_instance)
):
    task_dto: TaskDTO = await task_service.save(params=params)

    return JSONResponse(
        content=jsonable_encoder(task_dto),
        status_code=status.HTTP_201_CREATED
    )
