from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class PenjualanBase(BaseModel):
    id_pembeli: int = Field(None, example=1)
    id_produk: int = Field(None, example=1)
    total_harga: int = Field(..., gt=0, example=50000)
    waktu_penjualan: datetime = Field(..., example="2026-06-23T00:00:00")


class PenjualanCreate(PenjualanBase):
    pass


class PenjualanUpdate(BaseModel):
    id_pembeli: Optional[int] = Field(None, example=1)
    id_produk: Optional[int] = Field(None, example=1)
    total_harga: Optional[int] = Field(None, gt=0, example=50000)
    waktu_penjualan: Optional[datetime] = Field(None, example="2026-06-23T00:00:00")



class Penjualan(PenjualanBase):
    id_penjualan: int

    class Config:
        from_attributes = True
