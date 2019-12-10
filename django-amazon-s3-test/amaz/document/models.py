from django.db import models

from config.storage import PrivateMediaStorage


class Document(models.Model):
    file = models.FileField()
    uploaded = models.DateTimeField(auto_now_add=True)


class PrivateDocument(models.Model):
    file = models.FileField(storage=PrivateMediaStorage())
    uploaded = models.DateTimeField(auto_now_add=True)
