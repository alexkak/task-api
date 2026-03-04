from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str
    DEBUG: bool
    API_V1_PREFIX: str

    # Class Config tells pydantic-settings to read from the .env file
    # Withouth this, it only read from actual environment variables, not from the .env file.
    class Config:
        env_file = ".env"

settings = Settings()