import json
import pytest
import logging

from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}


@pytest.mark.asyncio
async def test_read_player():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/player/klose", params={"player_id": "1"})
        assert response.status_code == 200
        assert response.json() == {
            "id": "klose",
            "team": "werder",
            "description": "Kopf",
        }


@pytest.mark.asyncio
async def test_create_player():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
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


@pytest.mark.asyncio
async def test_update_player():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.put(
            "/players/update/",
            content=json.dumps(
                {
                    "id": "klose",
                    "team": "werder",
                    "description": "my hero!!"
                }
            )
        )
        logging.info(response)
        assert response.status_code == 200
        assert response.json() == {
            "id": "klose",
            "team": "werder",
            "description": "my hero!!"
        }


@pytest.mark.skip(reason="just skip")
async def test_skip():
    async with AsyncClient(base_url="localhost:8000") as ac:
        response = await ac.get(
            "/"
        )
        assert response.status_code == 200
        assert response.json() == {
            "msg": "success"
        }
