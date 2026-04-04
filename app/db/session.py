from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.config import settings


def _to_async_pg_url(url: str) -> str:
    """Map a sync Postgres URL to one SQLAlchemy can use with asyncpg.

    Alembic and local tools often use postgresql:// or postgresql+psycopg2://.
    The FastAPI app uses an async engine, which needs postgresql+asyncpg://.
    """
    if "+asyncpg" in url:
        return url
    if url.startswith("postgresql+psycopg2://"):
        return url.replace("postgresql+psycopg2://", "postgresql+asyncpg://", 1)
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+asyncpg://", 1)
    return url


class DatabaseProvider:
    def __init__(self) -> None:
        self.url = _to_async_pg_url(str(settings.database_url))
        self.engine = self._build_engine()
        self.session_factory = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    def get_engine_kwargs(self) -> dict:
        engine_kwargs: dict = {}

        if settings.environment == "local":
            engine_kwargs["echo"] = True

        if settings.environment == "production":
            engine_kwargs["pool_pre_ping"] = True

        return engine_kwargs

    def _build_engine(self):
        return create_async_engine(self.url, **self.get_engine_kwargs())

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db = DatabaseProvider()
SessionDep = Annotated[AsyncSession, Depends(db.get_session)]
