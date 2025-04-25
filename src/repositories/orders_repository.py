from typing import Any

from sqlalchemy import insert

from models.orders import orders
from repositories.abc_repositories import AbstractRepository
from schemas.order import OrderCreateSchema, OrderDatabase


class OrdersRepository(AbstractRepository):

    def __init__(self, session_maker: Any):
        self._session_maker = session_maker
        self.model = orders

    async def create(self, data: OrderCreateSchema) -> OrderDatabase:
        async with self._session_maker() as session:
            query = insert(self.model).values(data.model_dump(exclude_unset=True)).returning(self.model)
            result = await session.execute(query)
            await session.commit()

        return OrderDatabase.model_validate(result.fetchone(), from_attributes=True)

    async def update(self, **kwargs: dict) -> None:
        pass
