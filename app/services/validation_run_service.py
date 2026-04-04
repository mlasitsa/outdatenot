from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.repositories.validation_run import ValidationRunRepository

class ValidationRunService():
    def __init__(self, session: AsyncSession):
        self.validation_run_repository = ValidationRunRepository(session)

