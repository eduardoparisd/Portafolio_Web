from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.models.contact import Contact
from app.schemas.contact import ContactCreate


async def save_contact(db: AsyncSession, data: ContactCreate) -> Contact:
    """
    Guarda un nuevo mensaje de contacto en la base de datos.
    Retorna el objeto Contact creado con su ID y timestamp.
    """
    new_contact = Contact(
        name=data.name,
        email=data.email,
        message=data.message,
    )
    db.add(new_contact)
    await db.flush()        # obtiene el ID sin hacer commit aún
    await db.refresh(new_contact)
    return new_contact


async def get_contact_count_by_email(db: AsyncSession, email: str) -> int:
    """
    Cuenta cuántos mensajes se han recibido de un email.
    Usado para rate limiting básico a nivel de aplicación.
    """
    result = await db.execute(
        select(func.count()).where(Contact.email == email)
    )
    return result.scalar_one()