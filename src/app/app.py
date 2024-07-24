from typing import Any

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.get_log import router as log_router

def get_app_config() -> dict[str, Any]:
    """
    Load application configuration
    """

    config: dict[str, Any] = {
        "ttile": "gazprombank",
        "version": "0.1.0",
        "description": "Сервис разбора почтовых логов",
        "default_response_class": ORJSONResponse
    }

    return config

def create_app() -> FastAPI:
    """
        Create FastApi application
    """

    app: FastAPI = FastAPI(
        **get_app_config(),
    )

    app.include_router(log_router)

    return app


app: FastAPI = create_app()
