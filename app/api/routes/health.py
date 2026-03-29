from fastapi import APIRouter
from app.core.config import settings
from datetime import datetime

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
async def health():
    """
    Health check endpoint.
    """
    return {
        "status": "ok", 
        "app_name": settings.app_name or 'outdatenot', 
        "version": settings.version or "unknown",
        "timestamp": datetime.now().isoformat()
    }