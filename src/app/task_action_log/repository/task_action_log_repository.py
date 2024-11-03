from app.conf.repository.base_repository import BaseRepository
from .task_action_log_repository_interface import TaskActionLogRepositoryInterface
from ..model.task_action_log import TaskActionLog


class TaskActionLogRepository(TaskActionLogRepositoryInterface, BaseRepository):
    pass


task_action_log_repository = TaskActionLogRepository(TaskActionLog)
