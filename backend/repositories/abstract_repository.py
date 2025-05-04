from abc import ABC, abstractmethod
from contextlib import asynccontextmanager

from utils import AsyncSessionLocal

class Repositories(ABC):
    def __init__(self, session_factory = AsyncSessionLocal):
        self.session_factory = session_factory
        

    @asynccontextmanager
    async def session(self):
        session = self.session_factory()
        try:
            yield session
        finally:
            await session.close()
        
    @abstractmethod
    async def create(self,):
        raise NotImplementedError("Subclasses should implement this method.")

    @abstractmethod
    async def read_by_id(self,):
        raise NotImplementedError("Subclasses should implement this method.")
    
    @abstractmethod
    async def read_all(self):
        raise NotImplementedError("Subclasses should implement this method.")