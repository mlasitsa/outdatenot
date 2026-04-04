from app.db.repositories.BaseRepository import BaseRepository
from app.models.Installation import Installation
from sqlmodel import select
from typing import Optional


class InstallationRepository(BaseRepository[Installation]):
    
    
    def get_by_serial_number(self, serial_number: str) -> Optional[Installation]:
        """Fetch an installation by its serial number."""
        statement = select(self.model).where(self.model.serial_number == serial_number)
        return self.session.exec(statement).first()
    

    