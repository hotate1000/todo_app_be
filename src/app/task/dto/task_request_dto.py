from app.conf.dto import BaseDTO
from datetime import date, datetime


class TaskRequestDTO(BaseDTO):

    distributor_user_id: int
    recipient_user_id: int
    content: str
    deadline_at: date
    completed_at: datetime
    is_deleted: bool = False
