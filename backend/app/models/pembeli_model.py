from pydantic import BaseModel, Field
from typing import Optional


class PembeliBase(BaseModel):
    nama_pembeli: str = Field(..., max_length=255, example="Budi Santoso")


class PembeliCreate(PembeliBase):
    pass


class PembeliUpdate(BaseModel):
    nama_pembeli: Optional[str] = Field(None, max_length=255, example="Budi Santoso")


class Pembeli(PembeliBase):
    id_pembeli: int

    class Config:
        from_attributes = True
