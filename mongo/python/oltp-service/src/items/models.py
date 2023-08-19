from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, UUID4
from src.db import MongoBase


class Category(str, Enum):
    """Category of an item."""

    TOOLS = "tools"
    CONSUMABLES = "consumables"


# -----------------------------------------------------------------------------
#
class ItemPayload(MongoBase):
    """Representation of an item payload in the system."""

    count: int = Field(ge=0, description="Number of this item in stock")
    price: float = Field(gt=0.0, description="Price of the item in Euro")
    category: Category = Field(description="Category this item belongs to")
    name: str = Field(min_length=1, max_length=8, description="Name of the item")


class ItemSchema(ItemPayload):
    """Representation of an item in the system."""

    id: UUID4 = Field(description="Unique identifier (UUID) that specifies this item")


# -----------------------------------------------------------------------------
#
class QueryArguments(BaseModel):
    """Representation of item query arguments in the system."""

    name: Optional[str] = None
    count: Optional[int] = None
    price: Optional[float] = None
    category: Optional[Category] = None


class ItemArgumentResponse(BaseModel):
    """Representation of an argument query response in the system."""

    query: QueryArguments = Field(
        description="Dictionary containing the user's query arguments"
    )
    selection: List[ItemSchema] = Field(
        description="List of items that match the query arguments"
    )
