from .user_service_interface import UserServiceInterface
from threading import Lock
from typing import List
from core.db import Transactional
from ..dto import UserDTO, UserRequestDTO
from ..model.user import User
from ..repository.user_repository import user_repository


class UserService(UserServiceInterface):
    _instance = None
    _lock = Lock()

    def __new__(cls):
        raise NotImplementedError("直接インスタンスを作成することは出来ません")

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = cls.__internal_new__()
            return cls._instance

    @Transactional()
    async def find_all(self) -> List[UserDTO]:
        user_models: List[User] = await user_repository.find_all()

        user_dtos: List[UserDTO] = [UserDTO.model_validate(user_model) for user_model in user_models]

        return user_dtos

    @Transactional()
    async def save(self, params: UserRequestDTO) -> UserDTO:
        user_model: User = User(**params.model_dump())

        result: User = await user_repository.save(user_model)

        user_dto: UserDTO = UserDTO.model_validate(result)

        return user_dto
