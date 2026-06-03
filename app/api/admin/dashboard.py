from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import os

from app.core.database import get_db
from app.models.user import User

router = APIRouter()


@router.get("/")
async def admin_root():
    html_path = os.path.join(os.path.dirname(__file__), "../../backoffice/index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@router.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).order_by(User.created_at.desc()))
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
