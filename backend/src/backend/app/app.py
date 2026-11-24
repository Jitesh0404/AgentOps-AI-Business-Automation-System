import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def test():
    return {"status": 200, "message": "All okk"}


def main():
    print("Main function executed")

    uvicorn.run("backend.app.app:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
