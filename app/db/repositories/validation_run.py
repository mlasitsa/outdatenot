from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.models.validation_run import ValidationRunModel
from app.db.repositories.base import BaseRepository

class ValidationRunRepository(BaseRepository[ValidationRunModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, ValidationRunModel)
