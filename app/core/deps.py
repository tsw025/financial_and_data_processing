from sqlalchemy.ext.asyncio import AsyncSession

from core.db import AsyncSessionLocal


async def get_async_session() -> AsyncSession:
    """Factory method returns an async session for use in the DI system."""
    async with AsyncSessionLocal() as session:
        yield session
