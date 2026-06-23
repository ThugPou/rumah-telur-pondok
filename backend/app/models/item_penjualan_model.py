from pydantic import BaseModel, Field
from typing import Optional


class ItemPenjualanBase(BaseModel):
    id_penjualan: int = Field(..., example=1)
    id_produk: int = Field(..., example=1)
    jumlah: int = Field(..., gt=0, example=2)
    harga_satuan: int = Field(..., gt=0, example=25000)
    subtotal: int = Field(..., gt=0, example=50000)


class ItemPenjualanCreate(ItemPenjualanBase):
    pass


class ItemPenjualanUpdate(BaseModel):
    id_penjualan: Optional[int] = Field(None, example=1)
    id_produk: Optional[int] = Field(None, example=1)
    jumlah: Optional[int] = Field(None, gt=0, example=2)
    harga_satuan: Optional[int] = Field(None, gt=0, example=25000)
    subtotal: Optional[int] = Field(None, gt=0, example=50000)


class ItemPenjualan(ItemPenjualanBase):
    id: int

    class Config:
        from_attributes = True
