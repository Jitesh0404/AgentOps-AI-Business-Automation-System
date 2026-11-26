import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from backend.database.connection import check_database_connection, get_db
from backend.handler.error import Error
from backend.handler.error_handler import AppException, app_exception_handler
from backend.handler.messages import BAD_REQUEST, OK
from backend.handler.status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST
from backend.routes.feedback import router as feedback_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(AppException, app_exception_handler)


@app.get("/health/{id}")
def test(id: int):

    if id != 1:
        raise AppException(Error(status_code=HTTP_400_BAD_REQUEST, message=BAD_REQUEST))

    return {"status": HTTP_200_OK, "message": OK, "data": {"key": "test key"}}


@app.get("/database-test")
def database_test(db: Session = Depends(get_db)):
    return {"message": "Database session created"}


app.include_router(feedback_router, prefix="/api/v1")


def main():
    uvicorn.run("backend.app.app:app", host="0.0.0.0", port=8000, reload=True)
    try:
        check_database_connection()
        print("PostgreSQL connected successfully!")

    except Exception as error:
        print(f"Database connection failed: {error}")


if __name__ == "__main__":
    main()
