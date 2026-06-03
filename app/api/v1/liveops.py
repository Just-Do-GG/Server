from fastapi import APIRouter

router = APIRouter()


@router.get("/config")
async def get_config():
    return {"features": {}}


@router.get("/features")
async def get_features():
    return {"flags": []}
