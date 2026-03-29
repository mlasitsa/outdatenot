from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.health import router as health_router

app = FastAPI(title="outdatenot")

app.include_router(health_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "message": settings
    }