from pydantic_settings import BaseSettings
from pydantic import Field

class AppConfig(BaseSettings):
    host: str = Field(default="0.0.0.0", alias="APP_HOST")
    port: int = Field(default="8080", alias="APP_PORT")
    app_module: str = Field(default="app.main", alias="APP_MODULE")

config = AppConfig()
