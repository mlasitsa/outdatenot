from db.models.repository import RepositoryModel
from db.repositories.base import BaseRepository
from sqlmodel import Session

class RepositoryRepository(BaseRepository[RepositoryModel]):
    def __init__(self, session: Session) -> None:
        super().__init__(session, RepositoryModel)

