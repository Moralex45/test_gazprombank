
from collections.abc import AsyncGenerator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from core.config import get_settings_instance

Base = declarative_base()

async_engine = create_async_engine(
    get_settings_instance().get_database_url,
    echo=True,
    future=True,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:

    async_session = async_sessionmaker(
        async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with async_session() as session:
        yield session
