from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime
import re


class ContactCreate(BaseModel):
    """Schema de entrada — lo que manda el formulario de Reflex."""
    name: str
    email: EmailStr
    message: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        if len(v) > 100:
            raise ValueError("El nombre no puede superar los 100 caracteres.")
        return v

    @field_validator("message")
    @classmethod
    def validate_message(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 10:
            raise ValueError("El mensaje debe tener al menos 10 caracteres.")
        if len(v) > 2000:
            raise ValueError("El mensaje no puede superar los 2000 caracteres.")
        return v

    @field_validator("email")
    @classmethod
    def validate_email_format(cls, v: str) -> str:
        # Pydantic EmailStr ya valida, esto es una capa extra
        v = v.strip().lower()
        return v


class ContactResponse(BaseModel):
    """Schema de salida — lo que devuelve la API."""
    id: int
    name: str
    email: str
    message: str
    created_at: datetime

    model_config = {"from_attributes": True}


class ContactSuccessResponse(BaseModel):
    """Respuesta simple de éxito para el frontend."""
    success: bool
    message: str