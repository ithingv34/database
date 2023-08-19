# Third party modules
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


# ---------------------------------------------------------
#
class Configuration(BaseSettings):
    """Configuration parameters."""

    # project
    name: str
    version: str

    mongo_url: str


# ---------------------------------------------------------

# Note that the ".env" file is always implicitly loaded.
# ENV_FILE environment value is set by uvicorn configuration in file run.py.
load_dotenv()

app_config = Configuration()
""" Configuration parameters instance. """
