from core.db import Base
from sqlalchemy import Integer, BigInteger, String, DateTime, Enum, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.schema import ForeignKey
from datetime import datetime
from ..constant.action_type import ActionType


class TaskActionLog(Base):
    __tablename__ = "task_action_log"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("user.id"), nullable=False, index=True, comment="実行者")
    task_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("task.id"), nullable=False, index=True, comment="タスク")
    action_type: Mapped[Enum] = mapped_column(Enum(ActionType), nullable=True, comment="内容")
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now(), server_default=func.now(), nullable=False, comment="作成日")

    user = relationship("User", uselist=False, foreign_keys=[user_id])
    task = relationship("Task", uselist=False, foreign_keys=[task_id])
