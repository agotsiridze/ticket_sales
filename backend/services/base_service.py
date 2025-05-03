from abc import ABC, abstractmethod

class ServiceBase(ABC):
   
    @abstractmethod 
    async def create(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    @abstractmethod 
    async def read_by_id(self, user_id: str):
        raise NotImplementedError("Subclasses should implement this method.")
    
    @abstractmethod    
    async def read_all(self):
        raise NotImplementedError("Subclasses should implement this method.")