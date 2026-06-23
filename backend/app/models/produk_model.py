from pydantic import BaseModel, Field
from typing import Optional


class ProdukBase(BaseModel):
    nama_produk: str = Field(..., max_length=50, example="Telur Ayam")
    satuan: str = Field(..., max_length=10, example="kg")
    harga_satuan: int = Field(..., gt=0, example=25000)
    stok_tersedia: Optional[int] = Field(None, ge=0, example=100)


class ProdukCreate(ProdukBase):
    pass


class ProdukUpdate(BaseModel):
    nama_produk: Optional[str] = Field(None, max_length=50, example="Telur Ayam")
    satuan: Optional[str] = Field(None, max_length=10, example="kg")
    harga_satuan: Optional[int] = Field(None, gt=0, example=25000)
    stok_tersedia: Optional[int] = Field(None, ge=0, example=100)


class Produk(ProdukBase):
    id_produk: int

    class Config:
        from_attributes = True
