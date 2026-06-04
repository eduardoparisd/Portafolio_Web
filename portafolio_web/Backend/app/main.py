from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.db.database import create_tables
from app.api.v1.contact import router as contact_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup / Shutdown events."""
    await create_tables()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend API para portafolio NetDevOps — Eduardo Paris",
    lifespan=lifespan,
)

# CORS: solo permite peticiones desde el frontend Reflex
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# Routers
app.include_router(contact_router, prefix="/api/v1")


@app.get("/health", tags=["Health"])
async def health_check():
    """Endpoint de health check para Nginx y Docker."""
    return {"status": "ok", "service": settings.PROJECT_NAME}
