from fastapi import APIRouter, Depends
from app.api.deps import admin_required
from app.core.database import SessionLocal
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/users")
def get_all_users(admin=Depends(admin_required)):
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users
