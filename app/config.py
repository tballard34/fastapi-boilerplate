from pydantic import Field
from pydantic_settings import BaseSettings

from app.models import EnvironmentType, LogLevelType


class Settings(BaseSettings):
    environment: EnvironmentType = Field(
        default="dev",
        description="Environment (dev/staging/prod)",
    )

    # Logging
    log_level: LogLevelType = Field(default="INFO", description="Logging level")

    # Example environment variable
    env_var_name: str = Field(default="", description="Example environment variable")

    class Config:
        env_file: str = ".env"
        env_file_encoding: str = "utf-8"
        case_sensitive: bool = False


# Global settings instance - validates on import
settings: Settings = Settings()
