from celery import Celery
from src.configuration.celery_config import CeleryConfig

app = Celery("task", broker=CeleryConfig.broker_url)
