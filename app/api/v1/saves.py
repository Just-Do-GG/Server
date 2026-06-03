from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_saves():
    return {"saves": []}


@router.post("/")
async def save_game():
    return {"status": "ok"}


@router.get("/{save_id}")
async def get_save(save_id: str):
    return {"save_id": save_id}
