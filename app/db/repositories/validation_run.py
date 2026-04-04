from sqlmodel import Session
from app.db.models.validation_run import ValidationRunModel
from app.db.repositories.base import BaseRepository

class ValidationRunRepository(BaseRepository[ValidationRunModel]):
    def __init__(self, session: Session):
        super().__init__(session, ValidationRunModel)
