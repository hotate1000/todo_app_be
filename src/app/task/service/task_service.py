from threading import Lock
from typing import List
from core.db import Transactional
from .task_service_interface import TaskServiceInterface
from ..dto import TaskDTO, TaskRequestDTO
from ..model.task import Task
from ..repository.task_repository import task_repository


class TaskService(TaskServiceInterface):
    _instance = None
    _lock = Lock()

    def __new__(cls):
        raise NotImplementedError("直接インスタンスを作成することは出来ません")

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = cls.__internal_new__()
        return cls._instance

    @Transactional()
    async def find_all(self) -> List[TaskDTO]:
        task_models: List[Task] = await task_repository.find_all()

        task_dtos: List[TaskDTO] = [TaskDTO.model_validate(task_model) for task_model in task_models]

        return task_dtos

    @Transactional()
    async def save(self, params: TaskRequestDTO) -> TaskDTO:
        task_model: Task = Task(**params.model_dump())

        result: Task = await task_repository.save(task_model)

        task_dto: TaskDTO = TaskDTO.model_validate(result)

        return task_dto
