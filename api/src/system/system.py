from fastapi import APIRouter, Depends
from src.system.config import get_settings, Settings

router = APIRouter()

@router.get(
    path="/",
    summary="Retrieve system state.",
    description="""
        Used to extract system environment variables.
    """
)
async def main(settings: Settings = Depends(get_settings)):
    return settings