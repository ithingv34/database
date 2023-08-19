from bson import ObjectId
from typing import Callable

from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

# Local program modules
from src.config import app_config


# Pydantic models...
class MongoBase(BaseModel):
    """Class that handles conversions between MongoDB '_id' key and our own 'id' key.

    MongoDB uses `_id` as an internal default index key. We can use that to our advantage.
    """

    class Config:
        """basic config."""

        from_attributes = True
        populate_by_name = True

    # noinspection PyArgumentList
    @classmethod
    def from_mongo(cls, data: dict) -> Callable:
        """Convert "_id" (str object) into "id" (UUID object)."""

        if not data:
            return data

        mongo_id = data.pop("_id", None)
        return cls(**dict(data, id=mongo_id))

    def to_mongo(self, **kwargs) -> dict:
        """Convert "id" (UUID object) into "_id" (str object)."""

        parsed = self.model_dump(**kwargs)

        if "_id" not in parsed and "id" in parsed:
            parsed["_id"] = str(parsed.pop("id"))

        return parsed


# ---------------------------------------------------------
#
class Engine:
    """MongoDb database async engine class.


    :type db: C{motor.motor_asyncio.AsyncIOMotorDatabase}
    :ivar db: AsyncIOMotorDatabase class instance.
    :type connection: C{motor.motor_asyncio.AsyncIOMotorClient}
    :ivar connection: AsyncIOMotorClient class instance.
    """

    db: AsyncIOMotorDatabase = None
    connection: AsyncIOMotorClient = None

    # ---------------------------------------------------------
    #
    @classmethod
    async def connect_to_mongo(cls):
        """Initialize DB connection to MongoDb and database."""

        cls.connection = AsyncIOMotorClient(app_config.mongo_url)
        cls.db = cls.connection.api_db

    # ---------------------------------------------------------
    #
    @classmethod
    async def close_mongo_connection(cls):
        """Close DB connection."""

        cls.connection.close()
