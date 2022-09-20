from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

fake_db = {
    "klose": {"id": "klose", "team": "werder", "description": "Kopf"},
    "podolski": {"id": "podolski", "team": "koeln", "description": "National elf"},
}


class Player(BaseModel):
    id: str
    team: str
    description: Optional[str] = None


@app.get("/")
async def read_root():
    return {"msg": "Hello World"}


@app.get("/player/{player_id}", response_model=Player)
async def read_player(player_id: str):
    return fake_db.get(player_id, None)


@app.post("/players/", response_model=Player)
async def create_player(player: Player):
    if player.id in fake_db:
        raise HTTPException(status_code=400, detail="player already exists")

    fake_db[player.id] = player
    return player


@app.put("/players/update/", response_model=Player)
async def update_player(player: Player):
    if player.id not in fake_db:
        raise HTTPException(status_code=400, detail="player already exists")
    fake_db[player.id] = player
    return player
