from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class PengeluaranBase(BaseModel):
    jenis_pengeluaran: str = Field(None, max_length=25, example="Bahan Baku")
    jumlah_pengeluaran: int = Field(None, gt=0, example=150000)
    waktu_pengeluaran: datetime = Field(None, example="2026-06-23T00:00:00")
    foto_struk: Optional[str] = Field(None, example="struk_20260623.jpg")


class PengeluaranCreate(PengeluaranBase):
    pass


class PengeluaranUpdate(BaseModel):
    jenis_pengeluaran: Optional[str] = Field(None, max_length=25, example="Bahan Baku")
    jumlah_pengeluaran: Optional[int] = Field(None, gt=0, example=150000)
    waktu_pengeluaran: Optional[datetime] = Field(None, example="2026-06-23T00:00:00")
    foto_struk: Optional[str] = Field(None, example="struk_20260623.jpg")


class Pengeluaran(PengeluaranBase):
    id_pengeluaran: int

    class Config:
        from_attributes = True
