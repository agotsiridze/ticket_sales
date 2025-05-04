from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    async def create(self):
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    async def read_by_id(self):
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    async def read_all(self):
        raise NotImplementedError("Subclasses must implement this method")
