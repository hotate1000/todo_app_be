from core.db import Base
from app.conf.model.timestamp import TimeStamp
from sqlalchemy.schema import ForeignKey
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import text


class User(Base, TimeStamp):
  __tablename__ = "user"

  id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
  email: Mapped[String] = mapped_column(String(255), nullable=False, index=True, comment="メールアドレス")
  last_name: Mapped[String] = mapped_column(String(50), nullable=False, comment="苗字")
  first_name: Mapped[String] = mapped_column(String(50), nullable=False, comment="名前")
  is_active: Mapped[Boolean] = mapped_column(Boolean, default=False, server_default=text("0"), nullable=False, index=True, comment="アクティブ")
  slack_id: Mapped[String] = mapped_column(String(50), nullable=True, comment="スラックID")
