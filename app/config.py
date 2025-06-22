from pydantic_settings import BaseSettings
from pydantic import Field
import enum


class EnvironmentEnum(enum.Enum):
    local = "LOCAL"
    development = "DEV"
    stage = "STAGE"
    PRODUCTION = "PROD"


class AppConfig(BaseSettings):
    host: str = Field(default="0.0.0.0", alias="APP_HOST")
    port: int = Field(default="8080", alias="APP_PORT")
    environment: EnvironmentEnum = Field(
        default=EnvironmentEnum.local,
        alias="APP_ENVIRONMENT",
    )
    app_module: str = Field(default="app.main", alias="APP_MODULE")

    @property
    def reload(self) -> bool:
        return self.environment == EnvironmentEnum.local


config = AppConfig()
