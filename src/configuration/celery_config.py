from src.configuration import config


class CeleryConfig:
    broker_url = config.get("RABBITMQ", "amqp://localhost:5672")
