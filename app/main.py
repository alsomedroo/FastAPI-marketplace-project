from fastapi import FastAPI
from app.api import auth, products, admin

app = FastAPI(title="Campus Marketplace")

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(admin.router)

@app.get("/")
def health_check():
    return {"status": "running"}
