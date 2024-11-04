from threading import Lock
from typing import List
from core.db import Transactional
from .task_action_log_service_interface import TaskActionLogServiceInterface
from ..dto import TaskActionLogDTO, TaskActionLogRequestDTO
from ..model.task_action_log import TaskActionLog
from ..repository.task_action_log_repository import task_action_log_repository


class TaskActionLogService(TaskActionLogServiceInterface):
    _instance = None
    _lock = Lock()

    def __new__(cls):
        raise NotImplementedError("直接インスタンスを作成することは出来ません。")

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
    async def find_all(self) -> List[TaskActionLogDTO]:
        task_action_log_models: List[TaskActionLog] = await task_action_log_repository.find_all()

        task_action_log_dtos: List[TaskActionLogDTO] = [TaskActionLogDTO.model_validate(task_action_log_model.__dict__) for task_action_log_model in task_action_log_models]

        return task_action_log_dtos

    @Transactional()
    async def save(self, params: TaskActionLogRequestDTO) -> TaskActionLogDTO:
        task_action_log_model: TaskActionLog = TaskActionLog(**params.model_dump())

        result: TaskActionLog = await task_action_log_repository.save(task_action_log_model)

        task_action_log_dto: TaskActionLogDTO = TaskActionLogDTO.model_validate(result.__dict__)

        return task_action_log_dto
