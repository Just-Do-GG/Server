from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1 import auth, saves, liveops
from app.api.admin import dashboard

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    docs_url="/docs" if settings.DEBUG else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(saves.router, prefix="/api/v1/saves", tags=["Saves"])
app.include_router(liveops.router, prefix="/api/v1/liveops", tags=["LiveOps"])
app.include_router(dashboard.router, prefix="/api/admin", tags=["Admin"])


@app.get("/health")
async def health():
    return {"status": "ok", "version": settings.VERSION}
