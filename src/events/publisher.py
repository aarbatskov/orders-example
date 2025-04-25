import logging

from aiokafka import AIOKafkaProducer

from events.schemas import KafkaEventBase, OrderCreateEvent
from settings import Settings

logger = logging.getLogger(__name__)


class KafkaProducerBase:
    def __init__(self, settings: Settings):
        self._settings = settings
        self._producer = AIOKafkaProducer(bootstrap_servers=self._settings.kafka.kafka_url)

    async def start(self) -> None:
        await self._producer.start()
        logging.info("Kafka producer started")
        return None

    async def stop(self) -> None:
        if self._producer:
            await self._producer.stop()
            logging.info("Kafka producer stopped")
        return None

    async def send(self, topic: str, message: KafkaEventBase) -> None:
        if not self._producer:
            raise RuntimeError("Kafka producer not started")
        await self._producer.send_and_wait(topic, message.to_kafka_bytes())

        return None


class OrderProducer:
    def __init__(self, kafka: KafkaProducerBase) -> None:
        self._kafka = kafka

    async def publish_order(self, message: OrderCreateEvent) -> None:
        await self._kafka.send("orders_created", message)
        logging.info(f"Send event 'orders_created' {message.id}")

        return None
