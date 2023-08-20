from fastapi import FastAPI

# from src.core.database import db


app = FastAPI()


def create_app() -> FastAPI:
    # db.init()

    app = FastAPI()

    # @app.on_event("startup")
    # async def starup():
    #     await db.create_all()

    # @app.on_event("shutdown")
    # async def shutdown():
    #     await db.close()

    return app


app: FastAPI = create_app()


@app.get("/")
async def home() -> str:
    return "Server is running"
