from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.repositories.validation_step import ValidationStepRepository


class ValidationStepService():
    def __init__(self, session: AsyncSession):
        self.validation_step_repository = ValidationStepRepository(session)

