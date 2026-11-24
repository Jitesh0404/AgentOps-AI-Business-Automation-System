import uvicorn
from fastapi import FastAPI
from fastapi import status

from backend.handler.error import Error
from backend.handler.error_handler import AppException, app_exception_handler
from backend.handler.status_code import HTTP_400_BAD_REQUEST, HTTP_200_OK
from backend.handler.messages import BAD_REQUEST, OK

app = FastAPI()

app.add_exception_handler(AppException, app_exception_handler)


@app.get("/health/{id}")
def test(id: int):

    if id != 1:
        raise AppException(Error(status_code=HTTP_400_BAD_REQUEST, message=BAD_REQUEST))

    return {"status": HTTP_200_OK, "message": OK, "data": {"key": "test key"}}


def main():
    uvicorn.run("backend.app.app:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
