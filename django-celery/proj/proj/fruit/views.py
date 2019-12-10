import random
import string

from django.views.generic.base import RedirectView

from .tasks import create_fruit


class RegisterView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        fruit_name = generate_random_string()
        create_fruit.delay(name=fruit_name)
        return "http://localhost:8000/"


def generate_random_string(length=10):
    letters = [random.choice(string.ascii_lowercase) for _ in range(length)]
    return ''.join(letters)
