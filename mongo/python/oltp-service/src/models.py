from pydantic import BaseModel


class AlreadyExistError(BaseModel):
    """Define model for a http 409 exception (Conflict)."""

    detail: str = "Item already exists in DB"


class NotFoundError(BaseModel):
    """Define model for a http 404 exception (Not Found)."""

    detail: str = "Item not found in DB"


class NoArgumentsError(BaseModel):
    """Define model for a http 406 exception (Not Acceptable)."""

    detail: str = "No query arguments provided in URL"


class DbOperationFailedError(BaseModel):
    """Define model for a http 400 exception (Bad Request)."""

    detail: str = "DB operation failed"
