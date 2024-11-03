from app.conf.dto import BaseDTO
from ..constant.action_type import ActionType


class TaskActionLogRequestDTO(BaseDTO):

    user_id: int
    task_id: int
    action_type: ActionType
