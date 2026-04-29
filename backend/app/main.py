from fastapi import FastAPI
from backend.app.routers import translate, topics


def create_app() -> FastAPI:
    app = FastAPI(title="Parroty-POC Backend (FastAPI)")

    app.include_router(translate.router, prefix="/translate", tags=["translate"])
    app.include_router(topics.router, prefix="/topics", tags=["topics"])

    @app.get("/healthz")
    async def healthz():
        return {"status": "ok"}

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)

