from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProductCreate(BaseModel):
    title: str
    price: int
    image_url: Optional[str] = None

class ProductOut(BaseModel):
    id: int
    title: str
    price: int
    image_url: Optional[str]

    model_config = ConfigDict(from_attributes=True)
