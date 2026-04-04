from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.repositories.repository_settings import RepositorySettingsRepository

class RepositorySettingsService():
    def __init__(self, session: AsyncSession):
        self.repository_settings_repository = RepositorySettingsRepository(session)