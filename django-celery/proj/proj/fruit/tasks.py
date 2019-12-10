from celery import shared_task

from .models import Fruit


# Example: create_fruit.delay(name='apple')
@shared_task(name="create_fruit")
def create_fruit(name):
    Fruit.objects.update_or_create(name=name)
    return Fruit.objects.count()
