from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))
