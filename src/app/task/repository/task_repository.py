from app.conf.repository.base_repository import BaseRepository
from .task_repository_interface import TaskRepositoryInterface
from ..model.task import Task


class TaskRepository(TaskRepositoryInterface, BaseRepository):
    pass


task_repository = TaskRepository(Task)
