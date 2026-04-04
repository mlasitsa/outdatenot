from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.repositories.installation import InstallationRepository

class InstallationService():
    def __init__(self, session: AsyncSession):
        self.installation_repository = InstallationRepository(session)

    async def add_installation(self):
        pass 

    async def remove_installation(self):
        pass
        
