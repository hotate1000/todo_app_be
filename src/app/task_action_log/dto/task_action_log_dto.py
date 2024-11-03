from . import TaskActionLogRequestDTO
from datetime import datetime


class TaskActionLogDTO(TaskActionLogRequestDTO):

    id: int
    created_at: datetime
