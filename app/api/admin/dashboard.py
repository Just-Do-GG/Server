from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import os

from app.core.database import get_db
from app.models.user import User, GameConfig

router = APIRouter()


@router.get("/")
async def admin_root():
    html_path = os.path.join(os.path.dirname(__file__), "../../backoffice/index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@router.get("/games")
async def get_games(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(GameConfig).order_by(GameConfig.created_at.desc()))
    games = result.scalars().all()
    return [
        {
            "id": g.id,
            "game_id": g.game_id,
            "features": g.features,
            "created_at": g.created_at.isoformat(),
        }
        for g in games
    ]


@router.post("/games")
async def create_game(game_id: str, db: AsyncSession = Depends(get_db)):
    exists = await db.execute(select(GameConfig).where(GameConfig.game_id == game_id))
    if exists.scalar_one_or_none():
        return {"error": "Game already exists"}
    
    game = GameConfig(game_id=game_id, features={}, ads_keys={}, iap_products=[])
    db.add(game)
    await db.commit()
    return {"status": "ok", "game_id": game_id}


@router.get("/users")
async def get_users(game_id: str = None, db: AsyncSession = Depends(get_db)):
    query = select(User).order_by(User.created_at.desc())
    if game_id:
        query = query.where(User.game_id == game_id)
    result = await db.execute(query)
    users = result.scalars().all()
    return [
        {
            "id": u.id,
            "auth_type": u.auth_type,
            "game_id": u.game_id,
            "display_name": u.display_name,
            "created_at": u.created_at.isoformat(),
            "last_login": u.last_login.isoformat(),
        }
        for u in users
    ]
