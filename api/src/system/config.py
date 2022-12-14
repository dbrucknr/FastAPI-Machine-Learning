import logging
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = False
    version: str = "0.0.1"

def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()