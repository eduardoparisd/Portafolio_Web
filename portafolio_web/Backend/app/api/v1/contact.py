from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.contact import ContactCreate, ContactSuccessResponse
from app.services.contact_service import save_contact, get_contact_count_by_email
from app.core.config import settings

router = APIRouter(prefix="/contact", tags=["Contact"])


@router.post(
    "/",
    response_model=ContactSuccessResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Recibir mensaje de contacto",
    description="Recibe nombre, email y mensaje del formulario del portafolio y los persiste en PostgreSQL.",
)
async def create_contact(
    payload: ContactCreate,
    db: AsyncSession = Depends(get_db),
) -> ContactSuccessResponse:
    """
    POST /api/v1/contact/

    Body JSON:
        {
            "name": "Juan Pérez",
            "email": "juan@correo.com",
            "message": "Hola, me interesa colaborar..."
        }

    Returns:
        { "success": true, "message": "Mensaje recibido correctamente." }
    """
    # Rate limit básico: máx CONTACT_RATE_LIMIT mensajes por email
    count = await get_contact_count_by_email(db, payload.email)
    if count >= settings.CONTACT_RATE_LIMIT:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Has enviado demasiados mensajes. Intenta más tarde.",
        )

    await save_contact(db, payload)

    return ContactSuccessResponse(
        success=True,
        message="Mensaje recibido correctamente. Te contactaré pronto.",
    )


@router.get(
    "/health",
    tags=["Health"],
    summary="Health check del módulo de contacto",
)
async def contact_health():
    return {"status": "ok", "module": "contact"}