from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from app.core.config import SECRET_KEY, ALGORITHM
from app.core.database import SessionLocal
from app.models.user import User

def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    db.close()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def admin_required(user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    return user
