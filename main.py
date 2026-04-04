from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.health import router as health_router

app = FastAPI(title="outdatenot")

app.include_router(health_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "app_name": settings.app_name,
        "version": settings.version,
        "environment": settings.environment,
    }
