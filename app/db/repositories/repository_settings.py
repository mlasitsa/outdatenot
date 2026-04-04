from app.db.models.repository_settings import RepositorySettingsModel
from db.repositories.base import BaseRepository
from sqlmodel import Session

class RepositorySettingsRepository(BaseRepository[RepositorySettingsModel]):
    def __init__(self, session: Session) -> None:
        super().__init__(session, RepositorySettingsModel)
