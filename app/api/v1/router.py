from fastapi import APIRouter
from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.tasks import router as tasks_router

router = APIRouter()

router.include_router(health_router, tags=["health"])
router.include_router(tasks_router, tags=["tasks"])