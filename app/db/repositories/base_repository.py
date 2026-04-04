from typing import TypeVar, Generic, Type, List, Optional
from sqlmodel import Session, select, SQLModel
from typing import Any

T = TypeVar("T", bound=SQLModel)

class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session: Session = session
        self.model = model

    def get_one_by_id(self, id: int) -> Optional[T]:
        """Fetch a single record by ID."""
        return self.session.get(self.model, id)

    def get_all(self, filters: Any = None) -> List[T]:
        """Fetch all records for the model."""
        statement = select(self.model)

        if filters:
            statement = statement.where(*filters)

        return self.session.exec(statement).all()

    def create(self, obj: T) -> T:
        """Add and commit a new record."""
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def delete(self, id: int) -> bool:
        """Remove a record by ID."""
        obj = self.get_one_by_id(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            return True
        return False

