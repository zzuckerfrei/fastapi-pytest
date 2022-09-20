import logging

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_read_player():
    response = client.get("/player/klose", params={"player_id": "1"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "klose",
        "team": "werder",
        "description": "Kopf",
    }


def test_create_player():
    response = client.post(
        "/players/",
        json={"id": "Kruse", "team": "VFL", "description": "gambler"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "Kruse",
        "team": "VFL",
        "description": "gambler",
    }


def test_update_player():
    response = client.put(
        "/players/update/",
        json={"id": "klose", "team": "werder", "description": "my hero"}
    )
    logging.info(response)
    assert (response.status_code == 200)
    assert response.json() == {
        "id": "klose",
        "team": "werder",
        "description": "my hero"
    }
