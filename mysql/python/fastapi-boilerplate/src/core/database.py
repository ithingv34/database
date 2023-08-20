from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.config import config

Base = declarative_base()


class AsyncDatabaseSession:
    def __init__(self) -> None:
        self.session = None
        self.engine = None

    def init(self):
        self.engine = create_async_engine(config.DB_URL, future=True, echo=True)
        self.session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )()

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


db = AsyncDatabaseSession()
