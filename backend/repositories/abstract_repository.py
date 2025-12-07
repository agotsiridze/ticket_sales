from utils import AsyncSessionLocal, UnitOfWork


class Repository:
    def __init__(self, session_factory=AsyncSessionLocal):
        self.uow = UnitOfWork(session_factory)
