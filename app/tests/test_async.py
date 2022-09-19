import json
import pytest

from httpx import AsyncClient


@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}


@pytest.mark.asyncio
async def test_read_player():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/player/klose", params={"player_id": "1"})
        assert response.status_code == 200
        assert response.json() == {
            "id": "klose",
            "team": "werder",
            "description": "Kopf",
        }


@pytest.mark.asyncio
async def test_create_player():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post(
            "/players/",
            content=json.dumps(
                {
                    "id": "Kruse",
                    "team": "VFL",
                    "description": "gambler",
                }
            ),
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": "Kruse",
            "team": "VFL",
            "description": "gambler",
        }
