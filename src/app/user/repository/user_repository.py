from app.conf.repository.base_repository import BaseRepository
from .user_repository_interface import UserRepositoryInterface
from ..model.user import User


class UserRepository(UserRepositoryInterface, BaseRepository):
    pass


user_repository = UserRepository(User)
