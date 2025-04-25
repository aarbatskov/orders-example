from events.publisher import OrderProducer
from events.schemas import OrderCreateEvent
from repositories.orders_repository import OrdersRepository
from schemas.order import OrderCreateSchema, OrderResponse


class OrderService:

    def __init__(self, repository: OrdersRepository, producer: OrderProducer):
        self.repository = repository
        self.producer = producer

    async def create_order(self, data: OrderCreateSchema) -> OrderResponse:
        result = await self.repository.create(data)
        await self.producer.publish_order(
            message=OrderCreateEvent(id=result.id, user_id=result.user_id, total_price=result.total_price)
        )
        return OrderResponse(**result.model_dump())
