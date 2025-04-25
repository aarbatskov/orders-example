from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker as async_session_maker
from sqlalchemy.ext.declarative import declarative_base

from settings import get_settings

settings = get_settings()


engine = create_async_engine(settings.postgres.async_url, echo=True)
Base = declarative_base()

_async_session_maker = async_session_maker(engine, class_=AsyncSession, expire_on_commit=False)
