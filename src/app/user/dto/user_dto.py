from pydantic import ConfigDict
from datetime import datetime
from .user_request_dto import UserRequestDTO


class UserDTO(UserRequestDTO):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
