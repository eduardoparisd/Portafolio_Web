from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Proyecto
    PROJECT_NAME: str = "Portafolio API"
    VERSION: str = "1.0.0"

    # Base de datos PostgreSQL
    POSTGRES_USER: str = "portfolio_user"
    POSTGRES_PASSWORD: str = "changeme"
    POSTGRES_DB: str = "portfolio_db"
    POSTGRES_HOST: str = "db"        # nombre del servicio en Docker Compose
    POSTGRES_PORT: int = 5432

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # CORS — orígenes permitidos
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",     # Reflex dev
        "http://localhost:80",
        "https://eduardoparis.dev",  # dominio de producción (actualizar)
    ]

    # Rate limiting (contactos por IP por hora)
    CONTACT_RATE_LIMIT: int = 5

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()