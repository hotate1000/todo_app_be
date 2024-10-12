from  app.conf.dto import BaseDTO


class UserRequestDTO(BaseDTO):
    email: str
    last_name: str
    first_name: str
    is_active: bool = False
    slack_id: str | None = None
