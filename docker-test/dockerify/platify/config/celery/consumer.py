import os

from celery import Celery
from celery import bootsteps

from kombu import Consumer, Exchange, Queue


class Step(bootsteps.ConsumerStep):

    def get_consumers(self, channel):
        queue = Queue(name='custom', exchange=Exchange('custom'), routing_key='routing_key')
        return [
            Consumer(channel=channel, queues=[queue], callbacks=[self.handle_message], accept=['json']),
        ]

    def handle_message(self, body, message):
        print(f'Received:: Body: {body}; Message: {message};')
        message.ack()


app = Celery(broker=os.environ['RABBITMQ_URL_REMOTE'])
app.steps['consumer'].add(Step)
