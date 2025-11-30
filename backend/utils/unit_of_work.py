from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

class UnitOfWork:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory: async_sessionmaker[AsyncSession] = session_factory
        self.session: AsyncSession | None = None

    async def __aenter__(self) -> AsyncSession:
        self.session = self.session_factory()
        return self.session
    
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.session is None:
            return
            
        if exc_type is not None:
            await self.session.rollback()

        await self.session.close()