from typing import TypeVar, Generic, Type, List, Optional
from sqlmodel import select, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Any

T = TypeVar("T", bound=SQLModel)


class BaseRepository(Generic[T]):
    def __init__(self, session: AsyncSession, model: Type[T]):
        self.session: AsyncSession = session
        self.model = model

    async def get_one_by_id(self, id: int) -> Optional[T]:
        """Fetch a single record by ID."""
        return await self.session.get(self.model, id)

    async def get_all(self, filters: Optional[Any] = None) -> List[T]:
        """Fetch all records for the model."""
        statement = select(self.model)

        if filters:
            statement = statement.where(*filters)

        result = await self.session.exec(statement)

        return list(result.all())

    async def create(self, obj: T) -> T:
        """Add and commit a new record."""
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def delete(self, id: int) -> bool:
        """Remove a record by ID."""
        obj = await self.get_one_by_id(id)
        if obj:
            await self.session.delete(obj)
            await self.session.commit()
            return True
        return False
