from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.models.validation_step import ValidationStepModel
from app.db.repositories.base import BaseRepository

class ValidationStepRepository(BaseRepository[ValidationStepModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, ValidationStepModel)