from fastapi import FastAPI
from src.api.routes import router as api_router

app = FastAPI(title="Business Analyst AI Agent")

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"status": "ok", "service": "Business Analyst AI Agent"}
