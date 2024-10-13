from sqlalchemy import func, select, update, delete, desc, asc, insert, literal_column
from typing import TypeVar, Generic, Type, List
from sqlalchemy.orm import DeclarativeBase
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
        session.add(model)
        await session.flush()
        return model
