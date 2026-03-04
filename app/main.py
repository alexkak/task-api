from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.router import router

app = FastAPI()
app.include_router(router, prefix=settings.API_V1_PREFIX)
