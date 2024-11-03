from pydantic import ConfigDict
from datetime import datetime
from . import UserRequestDTO


class UserDTO(UserRequestDTO):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
