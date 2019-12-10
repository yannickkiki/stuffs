import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


app = Celery('config')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app.conf.beat_schedule = {
    # 'addiiiii': {
    #     'task': 'sum_two_numbers',
    #     'schedule': crontab(hour=7, minute=30, day_of_week=1),
    #     'args': (16, 16),
    # },
    # 'add-every-5-seconds': {
    #     'task': 'sum_two_numbers',
    #     'schedule': 30.0,
    #     'args': (16, 16)
    # },
    'sum-two-numbers': {
        'task': 'sum_two_numbers',
        'schedule': crontab(minute='*/20'),
        'args': (16, 16)
    },
}
