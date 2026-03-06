from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.core.config import settings
from app.api.v1.router import router
from app.core.exceptions import AppException
from app.core.error_handlers import app_exception_handler, validation_exception_handler

app = FastAPI()
app.include_router(router, prefix=settings.API_V1_PREFIX)
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
