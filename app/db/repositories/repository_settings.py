from app.db.models.repository_settings import RepositorySettingsModel
from app.db.repositories.base import BaseRepository
from sqlmodel.ext.asyncio.session import AsyncSession


class RepositorySettingsRepository(BaseRepository[RepositorySettingsModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, RepositorySettingsModel)
