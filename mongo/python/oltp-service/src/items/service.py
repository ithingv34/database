# BUILTIN modules
from typing import List

# Third party modules
from pydantic import UUID4
from pymongo.results import DeleteResult

from src.db import Engine
from src.items.models import ItemSchema, ItemPayload, QueryArguments


def _match(item: dict, args: QueryArguments) -> bool:
    """Check if the item matches the query arguments.

    Note that there is a check in the API layer that verifies that at
    least one of the query parameters have a value, so we don't need
    to do that here.

    :param item: Item object from the DB.
    :param args: URL query arguments.
    :return: match status.
    """

    return all(
        (
            args.name is None or item["name"] == args.name,
            args.price is None or item["price"] == args.price,
            args.count is None or item["count"] == args.count,
            args.category is None or item["category"] == args.category.value,
        )
    )


async def create(payload: ItemSchema) -> bool:
    """Create Item in DB collection api_db.items.

    :param payload: New Item payload.
    :return: DB create result.
    """

    response = await Engine.db.items.insert_one(payload.to_mongo())

    return response.acknowledged


async def read_all() -> List[ItemSchema]:
    """Read all existing Items in DB collection api_db.items.

    :return: List of found Items.
    """

    result = []

    async for item in Engine.db.items.find({}):
        result.append(ItemSchema.from_mongo(item))

    return result


# ---------------------------------------------------------
#
async def read(key: UUID4) -> ItemSchema:
    """Read Item for matching index key from DB collection api_db.items.

    :param key: Index key.
    :return: Found Item.
    """

    response = await Engine.db.items.find_one({"_id": str(key)})

    return ItemSchema.from_mongo(response)


# ---------------------------------------------------------
#
async def query(arguments: QueryArguments) -> List[ItemSchema]:
    """Read all Items that match the query arguments from DB collection api_db.items.

    :param arguments: Search arguments.
    :return: List of found Items.
    """

    result = []

    async for item in Engine.db.items.find({}):
        if _match(item, arguments):
            result.append(ItemSchema.from_mongo(item))

    return result


# ---------------------------------------------------------
#
async def update(payload: ItemSchema) -> bool:
    """Update Item in DB collection api_db.items.

    :param payload: Updated Item payload.
    :return: DB update result.
    """

    key = payload.id
    base = ItemPayload(**payload.model_dump())
    response = await Engine.db.items.update_one(
        {"_id": str(key)}, {"$set": {**base.model_dump()}}
    )

    return response.raw_result["updatedExisting"]


# ---------------------------------------------------------
#
async def delete(key: UUID4) -> DeleteResult:
    """Delete Item for matching index key from DB collection api_db.items.

    :param key: Index key.

    :return: DB delete result.
    """

    return await Engine.db.items.delete_one({"_id": str(key)})
