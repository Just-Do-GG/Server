from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def admin_root():
    return {"status": "BackOffice placeholder"}
