from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

from app.core.config import settings


class DatabaseProvider:
    def __init__(self):
        self.url = str(settings.database_url)
        self.engine = self.build_engine()

    def get_engine_kwargs(self) -> dict:
        engine_kwargs = {}

        if settings.environment == "local":
            engine_kwargs["echo"] = True

        if settings.environment == "production":
            engine_kwargs["pool_pre_ping"] = True

        return engine_kwargs

    def build_engine(self):
        return create_engine(self.url, **self.get_engine_kwargs())

    def get_session(self):
        with Session(self.engine) as session:
            yield session


db = DatabaseProvider()
SessionDep = Annotated[Session, Depends(db.get_session)]