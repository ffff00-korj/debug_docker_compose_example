from fastapi import FastAPI
from app.config import config

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        f"{config.app_module}:app",
        host=config.host,
        port=config.port,
        reload=True,
    )
