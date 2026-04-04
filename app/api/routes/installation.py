from fastapi import APIRouter
from app.core.config import settings
from datetime import datetime

router = APIRouter(prefix="/installation", tags=["installation"])


"""
Add installation endpoint.
"""
@router.get("{id}")
async def add_installation(id: str):

    # TODO: Create add installation logic
    pass 


"""
Remove installation endpoint.
"""
@router.get("{id}")
async def remove_installation(id: str):

    # TODO: Create remove installation logic
    pass 

