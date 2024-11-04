from pydantic import ConfigDict
from datetime import datetime
from . import UserRequestDTO


class UserDTO(UserRequestDTO):

    id: int
    created_at: datetime
    updated_at: datetime
