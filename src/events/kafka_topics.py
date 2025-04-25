from aiokafka.admin import NewTopic

KAFKA_TOPICS = [NewTopic("orders_created", 3, 1)]
