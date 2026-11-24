from fastapi import Request
from fastapi.responses import JSONResponse

from backend.handler.error import Error


class AppException(Exception):
    def __init__(self, error: Error):
        self.error = error


async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.error.status_code, content=exc.error.model_dump()
    )
