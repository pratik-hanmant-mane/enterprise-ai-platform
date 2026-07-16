from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Centralized application configuration.

    Values are loaded from environment variables or the .env file.
    """

    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    app_name: str = Field(
        default="Enterprise AI Platform",
        alias="APP_NAME"
    )

    app_version: str = Field(
        default="0.1.0",
        alias="APP_VERSION"
    )

    app_environment: str = Field(
        default="development",
        alias="APP_ENV"
    )

    debug: bool = Field(
        default=True,
        alias="DEBUG"
    )

    # ------------------------------------------------------------------
    # Database
    # ------------------------------------------------------------------
    database_url: str = Field(
        alias="DATABASE_URL"
    )

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------
    log_level: str = Field(
        default="INFO",
        alias="LOG_LEVEL"
    )

    # ------------------------------------------------------------------
    # Security
    # ------------------------------------------------------------------
    secret_key: str = Field(
        alias="SECRET_KEY"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    jwt_algorithm: str = Field(
        default="HS256",
        alias="JWT_ALGORITHM"
    )
    
    jwt_access_token_expire_minutes: int = Field(
        default=30,
        alias="JWT_ACCESS_TOKEN_EXPIRE_MINUTES"
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.

    The configuration is loaded only once during the application's lifetime.
    """
    return Settings()


settings = get_settings()