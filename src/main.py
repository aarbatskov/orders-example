from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from api.v1.orders import router as order_router
from depends import container
from events.create_topics import KafkaTopicManager
from events.kafka_topics import KAFKA_TOPICS
from events.publisher import KafkaProducerBase
from logging_config import setup_logging
from services.orders_service import OrderService
from settings import get_settings

settings = get_settings()
setup_logging()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    async with KafkaTopicManager(settings) as manager:
        await manager.create_topics(KAFKA_TOPICS)
    kafka: KafkaProducerBase = container.resolve(KafkaProducerBase)
    await kafka.start()
    yield


def create_application() -> FastAPI:
    app = FastAPI(
        name=settings.application.name,
        version=settings.application.version,
        lifespan=lifespan,
    )
    return app


app = create_application()
app.dependency_overrides = {
    OrderService: lambda: container.resolve(OrderService),
}

app.include_router(order_router)
