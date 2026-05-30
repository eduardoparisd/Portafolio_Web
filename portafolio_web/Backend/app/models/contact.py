from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.db.database import Base


class Contact(Base):
    """
    Tabla: contacts
    Guarda cada mensaje recibido del formulario de contacto.
    """
    __tablename__ = "contacts"

    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String(100), nullable=False)
    email      = Column(String(255), nullable=False, index=True)
    message    = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f"<Contact id={self.id} email={self.email}>"