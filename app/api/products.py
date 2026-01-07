from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.core.s3 import upload_image
from app.api.deps import get_current_user
from app.models.product import Product

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def list_products(
    search: str = Query(None),
    page: int = 1,
    limit: int = 10
):
    db = SessionLocal()
    query = db.query(Product)

    if search:
        query = query.filter(Product.title.ilike(f"%{search}%"))

    products = query.offset((page - 1) * limit).limit(limit).all()
    db.close()
    return products



@router.post("/upload-image")
def upload_product_image(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user)
):
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files allowed")

    image_url = upload_image(file.file)

    return {
        "message": "Image uploaded successfully",
        "image_url": image_url
    }
