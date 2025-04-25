from uuid import UUID

from pydantic import BaseModel


class OrderCreateSchema(BaseModel):
    user_id: UUID
    comment: str | None = None
    total_price: float


class OrderUpdateSchema(BaseModel):
    comment: str | None = None
    total_price: float | None = None


class OrderDatabase(BaseModel):
    id: UUID
    user_id: UUID
    comment: str | None = None
    total_price: float


class OrderResponse(BaseModel):
    id: UUID
    user_id: UUID
    comment: str | None = None
    total_price: float
