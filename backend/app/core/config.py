from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Parroty-POC Backend"
    DATABASE_URL: str = "sqlite:///./backend_dev.db"
    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()

