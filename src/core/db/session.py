from contextvars import ContextVar
from ..setting import get_setting
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, async_scoped_session


setting = get_setting()

session_context = ContextVar("session_context", default=None)

DB_URL = f"mysql+aiomysql://{setting.db_user}:{setting.db_password}@{setting.db_host}:{setting.db_port}/{setting.db_name}?charset=utf8mb4"


def create_engine_and_session_factory(database_url: str):
    # create_async_engine(): 非同期データベースエンジンを作成し、データベースとの接続を非同期で管理。
    engine = create_async_engine(
        database_url,
        echo=True,
        future=True
    )

    # async_sessionmaker(): 非同期セッションを作成し、セッションを通じて非同期でデータベース操作。
    session_factory = async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession
    )

    return session_factory


def setup():
    session_factory = create_engine_and_session_factory(DB_URL)
    session = async_scoped_session(session_factory, scopefunc=session_context.get)
    return session


session = setup()
