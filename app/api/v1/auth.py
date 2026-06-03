from fastapi import APIRouter

router = APIRouter()


@router.post("/guest")
async def guest_login():
    return {"token": "placeholder"}


@router.post("/google")
async def google_login():
    return {"token": "placeholder"}


@router.post("/apple")
async def apple_login():
    return {"token": "placeholder"}


@router.post("/refresh")
async def refresh_token():
    return {"token": "placeholder"}
