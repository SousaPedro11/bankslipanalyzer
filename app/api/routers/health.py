from typing import Dict

from fastapi import APIRouter

from app.api.schemas.health import Health

router = APIRouter()


@router.get("/health", response_model=Health)
def health() -> Dict[str, str]:
    """
    Route that returns Koper-API health
    """
    return {"status": "alive"}
