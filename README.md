# orders-example

quick start
git clone https://github.com/aarbatskov/orders-example.git
cd orders-example

Запуск служебных сервисов: БД, Zookeeper, Kafka
docker compose --profile infra up --build -d

Запуск сервиса:
docker compose --profile api up
