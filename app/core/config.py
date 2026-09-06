from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="GIGAHOUSE_",
        extra="ignore",
    )

    app_name: str = "GIGAHouse API"
    environment: str = "development"
    debug: bool = False
    database_url: str

@lru_cache
def get_settings() -> Settings:
    return Settings()

