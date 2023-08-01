from typing import Generator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session
from sqlalchemy.orm import sessionmaker

from app.core.db import async_engine
from app.core.models import Base
from core.deps import get_async_session


@pytest.fixture(scope="session")
def anyio_backend():
    """Set the anyio backend to asyncio for session scope fixtures."""
    return "asyncio"


@pytest.fixture(scope="session")
async def get_test_engine():
    """Initialize a test engine for a test postgres database."""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield async_engine
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def session(get_test_engine) -> AsyncSession:
    """Initialize an async scoped session, only existing for the duration of the test."""
    from asyncio import current_task

    async with get_test_engine.begin() as connection:
        AsyncScopedSession = async_scoped_session(
            sessionmaker(
                bind=connection,
                autocommit=False,
                autoflush=False,
                expire_on_commit=False,
                class_=AsyncSession,
            ),
            current_task,
        )
        yield AsyncScopedSession()
        await connection.rollback()


@pytest.fixture()
def override_get_session(session: AsyncSession):
    """Dependency override used for enforcing the same session throughout the lifetime of the app."""

    async def _override_get_session():
        yield session

    return _override_get_session


@pytest.fixture()
def app(override_get_session) -> FastAPI:
    """App fixture, used to initialize the AsyncClient."""
    from main import app

    app.dependency_overrides[get_async_session] = override_get_session
    return app


@pytest.fixture()
async def client(anyio_backend, app) -> Generator:
    """Return an async TestClient with a scoped async db session."""
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c
