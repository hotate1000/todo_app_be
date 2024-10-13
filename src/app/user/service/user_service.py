from .user_service_interface import UserServiceInterface
from threading import Lock
from src.core.db import Transactional
from ..dto import UserDTO, UserRequestDTO


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
    async def save(self, params: UserRequestDTO) -> UserDTO:
        
