import uvicorn
from fastapi import FastAPI
from backend.handler.error_handler import throw_error

app = FastAPI()


@app.get("/health/{id}")
def test():
    if id != 1:
        throw_error({"status_code": 400, "message": "Something went wrong"})
    return {"status": 200, "message": "All okk"}


def main():
    print("Main function executed")

    uvicorn.run("backend.app.app:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
