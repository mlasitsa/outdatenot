from app.db.repositories.base import BaseRepository
from app.db.models.installation import InstallationModel
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Optional


class InstallationRepository(BaseRepository[InstallationModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, InstallationModel)
    
    async def add_installation(self, data: InstallationModel) -> InstallationModel:
        installation = await self.create(data)
        return installation

    async def remove_installation(self, installation_id: int) -> bool:
        return await self.delete(installation_id)

