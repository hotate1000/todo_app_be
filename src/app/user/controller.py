from fastapi import APIRouter, status
from .dto import UserDTO, UserRequestDTO
from .service.user_service import UserService
from fastapi import APIRouter, Depends


user_router = APIRouter()


@user_router.post(
    "",
    name="作成",
    status_code=status.HTTP_201_CREATED)
async def save(
    params: UserRequestDTO,
    user_service: UserService = Depends(UserService.get_instance)
):
    user_dto: UserDTO = await user_service.save(params=params)
