from abc import ABC, abstractmethod

from schemas.order import OrderCreateSchema, OrderDatabase


class AbstractRepository(ABC):

    @abstractmethod
    async def create(self, data: OrderCreateSchema) -> OrderDatabase:
        raise NotImplementedError

    @abstractmethod
    async def update(self, **kwargs: dict) -> None:
        raise NotImplementedError
