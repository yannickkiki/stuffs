from django.db import models

# from caching.base import CachingManager, CachingMixin


class Product(models.Model):
    name = models.CharField(max_length=255)
