from fastapi import FastAPI
from app.api import auth

app = FastAPI(title="Campus Marketplace")

app.include_router(auth.router)

@app.get("/")
def health_check():
    return {"status": "running"}
