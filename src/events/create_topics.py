import logging
from typing import Any, Optional, Self, Type

from aiokafka.admin import AIOKafkaAdminClient, NewTopic

from settings import Settings

logger = logging.getLogger(__name__)


class KafkaTopicManager:

    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def __aenter__(self) -> Self:
        self.admin_client = AIOKafkaAdminClient(bootstrap_servers=self.settings.kafka.kafka_url)
        await self.admin_client.start()
        return self

    async def __aexit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Any
    ) -> None:
        if self.admin_client:
            await self.admin_client.close()

        return None

    async def create_topics(self, topics: list[NewTopic]) -> None:
        if not self.admin_client:
            raise RuntimeError("Admin client is not started")

        existing_topics = await self.admin_client.list_topics()
        topics_to_create = [topic for topic in topics if topic.name not in existing_topics]

        if not topics_to_create:
            logger.info("All topics already exist.")
            return

        await self.admin_client.create_topics(new_topics=topics_to_create)
        logger.info(f"Created topics: {[topic.name for topic in topics_to_create]}")

        return None
