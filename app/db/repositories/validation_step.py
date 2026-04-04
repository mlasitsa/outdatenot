from sqlmodel import Session
from app.db.models.validation_step import ValidationStepModel
from app.db.repositories.base import BaseRepository

class ValidationStepRepository(BaseRepository[ValidationStepModel]):
    def __init__(self, session: Session) -> None:
        super().__init__(session, ValidationStepModel)