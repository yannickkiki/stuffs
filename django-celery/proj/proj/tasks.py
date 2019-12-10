from celery import shared_task


# To run in background with celery: add.delay(x=1, y=3)
@shared_task(name="sum_two_numbers")
def add(x, y):
    return x + y
