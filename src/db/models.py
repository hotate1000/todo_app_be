from core.db import Base
from app.user.model.user import User


# metadata は、SQLAlchemy における テーブルやカラムの定義、制約、インデックスなど、データベースに関連する全ての情報を格納するオブジェクト
# SQLAlchemyはデータベースのスキーマを把握し、それに基づいてデータベースとのやり取りを行う
TARGET_METADATA = Base.metadata
