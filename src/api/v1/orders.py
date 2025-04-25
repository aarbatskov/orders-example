from fastapi import APIRouter, Depends

from depends import get_instance_from_container
from schemas.order import OrderCreateSchema, OrderResponse
from services.orders_service import OrderService

router = APIRouter(tags=["Orders"])


@router.post("/orders")
async def create_order(
    order: OrderCreateSchema,
    service: OrderService = Depends(get_instance_from_container(OrderService)),
) -> OrderResponse:
    result = await service.create_order(order)
    return result
