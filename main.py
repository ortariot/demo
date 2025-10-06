import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app")
