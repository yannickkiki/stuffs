from django.db import models

from .metacard import MetaCard


class TrellisCard(models.Model):
    metacard_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
