import os

from celery import Celery
from celery.schedules import crontab


app = Celery()
app.autodiscover_tasks(packages=['platify'])
app.conf.update(
    broker_url=os.environ['RABBITMQ_URL'],
    broker_pool_limit=0,
    beat_schedule={
        'sum_two_numbers': {
            'task': 'sum_two_numbers', 'schedule': crontab(minute='*/5'), 'args': (16, 16)
        }
    }
)
