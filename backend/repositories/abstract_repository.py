from abc import ABC, abstractmethod

from utils import AsyncSessionLocal, UnitOfWork

class Repositories(ABC):
    def __init__(self, session_factory = AsyncSessionLocal):
        self.uow = UnitOfWork(session_factory)

        
    @abstractmethod
    async def create(self,):
        raise NotImplementedError("Subclasses should implement this method.")

    @abstractmethod
    async def read_by_id(self,):
        raise NotImplementedError("Subclasses should implement this method.")
    
    @abstractmethod
    async def read_all(self):
        raise NotImplementedError("Subclasses should implement this method.")