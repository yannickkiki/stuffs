from pprint import pprint

from django.test import TestCase
from django.utils.timezone import now
from django.db import connection

from base.models import Product


def test_now_lazy_loading():
    qs1 = Product.objects.filter(created__lt=now())
    Product.objects.create(created=now())
    qs2 = Product.objects.filter(created__lt=now())
    print(qs1.count())
    print(qs2.count())
    pprint(connection.queries)
