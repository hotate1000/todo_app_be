from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from .dto import UserDTO, UserRequestDTO
from .service.user_service import UserService



user_router = APIRouter()


@user_router.get(
    "",
    name="一覧取得",
    status_code=status.HTTP_200_OK,
    response_model=List[UserDTO]
)
async def find_all(
    user_service: UserService = Depends(UserService.get_instance)
):
    user_dtos: List[UserDTO] = await user_service.find_all()

    return JSONResponse(
        content=jsonable_encoder(user_dtos),
        status_code=status.HTTP_200_OK
    )

@user_router.post(
    "",
    name="作成",
    status_code=status.HTTP_201_CREATED,
    response_model=UserDTO
)
async def save(
    params: UserRequestDTO,
    user_service: UserService = Depends(UserService.get_instance)
):
    user_dto: UserDTO = await user_service.save(params=params)

    return JSONResponse(
        content=jsonable_encoder(user_dto),
        status_code=status.HTTP_201_CREATED
    )
