from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from config import SETTINGS

async_engine = create_async_engine(SETTINGS.database_url)
AsyncSessionLocal = sessionmaker(
    async_engine, autocommit=False, autoflush=False, expire_on_commit=False, class_=AsyncSession
)
