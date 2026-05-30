from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator

from app.core.config import settings


class Base(DeclarativeBase):
    pass


# Motor async — se conecta a PostgreSQL vía asyncpg
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,       # True para ver SQL en logs (solo dev)
    pool_size=5,
    max_overflow=10,
)

# Fábrica de sesiones async
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def create_tables() -> None:
    """Crea las tablas al arrancar la app si no existen."""
    async with engine.begin() as conn:
        from app.models import contact  # noqa: F401 — registra el modelo
        await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency injection: sesión de DB por request."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise