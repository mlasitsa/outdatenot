from app.db.repositories.base import BaseRepository
from app.db.models.installation import InstallationModel
from sqlmodel import select, Session
from typing import Optional


class InstallationRepository(BaseRepository[InstallationModel]):
    def __init__(self, session: Session) -> None:
        super().__init__(session, InstallationModel)