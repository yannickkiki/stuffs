import random
import string

from django.views.generic.base import RedirectView

from .tasks import create_fruit


class RegisterView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        fruit_name = generate_random_string()
        create_fruit.delay(name=fruit_name)
        return "http://localhost:8000/"


class ProduceView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        import os
        from kombu import Connection, Exchange, Queue, Producer

        conn = Connection(os.environ['RABBITMQ_URL_REMOTE'])

        queue = Queue(name='custom', exchange=Exchange('custom'), routing_key='routing_key')

        producer = Producer(exchange=queue.exchange, channel=conn.channel(), routing_key=queue.routing_key)
        producer.publish(body={'hello': "zautreii"}, serializer='json', declare=[queue], retry=True)

        return "http://localhost:8000/"


def generate_random_string(length=10):
    letters = [random.choice(string.ascii_lowercase) for _ in range(length)]
    return ''.join(letters)
