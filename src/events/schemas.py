import json
from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class KafkaEventBase(BaseModel):
    def to_kafka_bytes(self) -> bytes:
        def default_serializer(obj: Any) -> Any:
            if isinstance(obj, UUID):
                return str(obj)
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError(f"Type {type(obj)} not serializable")

        return json.dumps(self.model_dump(), default=default_serializer).encode("utf-8")


class OrderCreateEvent(KafkaEventBase):
    id: UUID
    user_id: UUID
    total_price: float
