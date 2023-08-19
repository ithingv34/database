from fastapi import APIRouter

from src.items.views import router as items_router


router = APIRouter()

router.include_router(items_router)
