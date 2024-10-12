from sqlalchemy import DateTime, func
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime


class TimeStamp():
    @declared_attr
    def created_at(cls):
        return mapped_column(DateTime(timezone=True), default=datetime.now(), nullable=False, server_default=func.now())

    @declared_attr
    def updated_at(cls):
        return mapped_column(DateTime(timezone=True), default=datetime.now(), nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
