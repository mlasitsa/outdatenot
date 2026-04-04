from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.models.repository import RepositoryModel
from app.db.repositories.base import BaseRepository


class RepositoryRepository(BaseRepository[RepositoryModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, RepositoryModel)
