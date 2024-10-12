from .user_request_dto import UserRequestDTO
from datetime import datetime


class UserDTO(UserRequestDTO):
    id: int
    created_at: datetime
    updated_at: datetime
