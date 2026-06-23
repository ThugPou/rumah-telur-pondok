from pydantic import BaseModel, Field
from typing import Optional


class AdminBase(BaseModel):
    nama_admin: str = Field(..., max_length=100, example="Admin Utama")
    password_admin: str = Field(..., max_length=50, example="secret123")


class AdminCreate(AdminBase):
    pass


class AdminUpdate(BaseModel):
    nama_admin: Optional[str] = Field(None, max_length=100, example="Admin Utama")
    password_admin: Optional[str] = Field(None, max_length=50, example="secret123")


class Admin(AdminBase):
    id_admin: int

    class Config:
        from_attributes = True
