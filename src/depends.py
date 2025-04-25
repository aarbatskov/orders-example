from collections.abc import Callable
from typing import TypeVar

import punq

from db.db import _async_session_maker
from events.publisher import KafkaProducerBase, OrderProducer
from repositories.orders_repository import OrdersRepository
from services.orders_service import OrderService
from settings import get_settings


def create_container() -> punq.Container:
    settings = get_settings()
    container = punq.Container()
    container.register(OrdersRepository, instance=OrdersRepository(_async_session_maker))
    container.register(KafkaProducerBase, instance=KafkaProducerBase(settings))
    container.register(OrderProducer, instance=OrderProducer(container.resolve(KafkaProducerBase)))
    container.register(
        OrderService,
        instance=OrderService(container.resolve(OrdersRepository), container.resolve(OrderProducer)),
    )
    return container


container = create_container()

T = TypeVar("T")


def get_instance_from_container(cls: type[T]) -> Callable[..., T]:

    def wrapper() -> T:
        return container.resolve(cls)

    return wrapper
