import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock, patch

from app.main import app

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@pytest.mark.asyncio
async def test_create_contact_success():
    mock_contact = AsyncMock()
    mock_count = AsyncMock(return_value=0)

    with patch("app.api.v1.contact.save_contact", mock_contact), \
         patch("app.api.v1.contact.get_contact_count_by_email", mock_count):

        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/contact/",
                json={
                    "name": "Eduardo Paris",
                    "email": "eduardo@test.com",
                    "message": "Hola, me interesa colaborar en un proyecto.",
                },
            )

    assert response.status_code == 201
    data = response.json()
    assert data["success"] is True


@pytest.mark.asyncio
async def test_create_contact_rate_limit():
    mock_count = AsyncMock(return_value=10)  # supera el límite

    with patch("app.api.v1.contact.get_contact_count_by_email", mock_count):
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/contact/",
                json={
                    "name": "Spam Bot",
                    "email": "spam@test.com",
                    "message": "Mensaje de prueba para rate limit.",
                },
            )

    assert response.status_code == 429


@pytest.mark.asyncio
async def test_create_contact_invalid_email():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/api/v1/contact/",
            json={
                "name": "Eduardo",
                "email": "no-es-un-email",
                "message": "Mensaje de prueba.",
            },
        )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_contact_short_message():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/api/v1/contact/",
            json={
                "name": "Eduardo",
                "email": "eduardo@test.com",
                "message": "Corto",
            },
        )
    assert response.status_code == 422