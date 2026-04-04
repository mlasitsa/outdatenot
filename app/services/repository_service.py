from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.repositories.repository import RepositoryRepository

class RepositoryService():
    def __init__(self, session: AsyncSession):
        self.repository_repository = RepositoryRepository(session)
        