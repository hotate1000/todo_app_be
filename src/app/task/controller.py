from fastapi import APIRouter, status
from typing import List
from .dto import TaskDTO, TaskRequestDTO


task_router = APIRouter()


@task_router.get(
    "",
    name="一覧取得",
    status_code=status.HTTP_200_OK,
    response_model=List[TaskDTO]
)
