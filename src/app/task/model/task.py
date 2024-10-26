from core.db import Base
from sqlalchemy import Integer, String, Boolean, Date, DateTime, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import text
from sqlalchemy.schema import ForeignKey
from datetime import datetime


class Task(Base):
    __tablename__ = "task"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    distributor_user_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("user.id"), nullable=False, index=True, comment="配布者")
    recipient_user_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("user.id"), nullable=False, index=True, comment="受信者")
    content: Mapped[String] = mapped_column(String(500), nullable=True, comment="内容")
    deadline_at: Mapped[Date] = mapped_column(Date, nullable=True, comment="期限日")
    completed_at: Mapped[Date] = mapped_column(Date, nullable=True, comment="完了日")
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now(), server_default=func.now(), nullable=False, comment="作成日")
    is_deleted: Mapped[Boolean] = mapped_column(Integer, default=False, server_default=text("0"), nullable=False)

    distributor_user = relationship("User", uselist=False, foreign_keys=[distributor_user_id])
    recipient_user = relationship("User", uselist=False, foreign_keys=[recipient_user_id])
