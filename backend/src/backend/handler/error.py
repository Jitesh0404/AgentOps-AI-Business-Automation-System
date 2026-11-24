from pydantic import BaseModel
from typing import Any


class Error(BaseModel):
    status_code: int = 500
    message: str = "Server not found"
    data: Any | None = None
