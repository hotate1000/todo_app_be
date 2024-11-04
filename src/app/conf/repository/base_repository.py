from sqlalchemy import func, select, update, delete, desc, asc, insert, literal_column
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase
from fastapi import HTTPException, status
from typing import TypeVar, Generic, Type, List
from core.db import session


# DeclarativeBase は、SQLAlchemyのモデル（テーブルのマッピング）を定義するための基底クラス
ModelType = TypeVar("ModelType", bound=DeclarativeBase)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def find_all(self) -> List[ModelType]:
        query = select(self.model).order_by(asc(self.model.id))
        result = await session.execute(query)
        return result.scalars().all()

    async def save(self, model: ModelType) -> ModelType:
        try:
            session.add(model)
            await session.flush()
            return model
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"INSERT時にエラーが発生しました。{e}"
            )
