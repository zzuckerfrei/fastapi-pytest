from fastapi.testclient import TestClient

from app.main import app

"""
이제 세가지 API 함수에 대해 테스트하는 함수들을 작성하겠습니다.

test_root(): “root“ API 함수에 대해 GET 방식으로 요청하여 테스트하는 함수 입니다.

test_read_item(): “read_item“ API 함수에 대해 item_id가 1인 item을 params 값에 추가하여 GET 방식으로 요청하여 테스트하는 함수 입니다.

test_create_item(): “create_item“ API 함수에 대해 생성할 item을 json 값에 추가하여 POST 방식으로 요청하여 테스트하는 함수 입니다.
"""

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