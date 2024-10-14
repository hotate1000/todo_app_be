from pydantic import ConfigDict
from .user_request_dto import UserRequestDTO
from datetime import datetime


class UserDTO(UserRequestDTO):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
