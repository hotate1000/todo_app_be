from core.db import Base
from app.user.model.user import User
from app.task.model.task import Task
from app.task_action_log.model.task_action_log import TaskActionLog

# metadata は、SQLAlchemy における テーブルやカラムの定義、制約、インデックスなど、データベースに関連する全ての情報を格納するオブジェクト
# SQLAlchemyはデータベースのスキーマを把握し、それに基づいてデータベースとのやり取りを行う
TARGET_METADATA = Base.metadata
