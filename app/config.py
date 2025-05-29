from pydantic import ConfigDict, Field
from pydantic_settings import BaseSettings

from app.models import EnvironmentType, LogLevelType


class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )

    environment: EnvironmentType = Field(
        default="dev",
        description="Environment (dev/staging/prod)",
    )

    # Logging
    log_level: LogLevelType = Field(default="INFO", description="Logging level")

    # Example environment variable
    env_var_name: str = Field(default="", description="Example environment variable")


# Global settings instance - validates on import
settings: Settings = Settings()
