from . import TaskRequestDTO
from datetime import datetime


class TaskDTO(TaskRequestDTO):

    id: int
    created_at: datetime
