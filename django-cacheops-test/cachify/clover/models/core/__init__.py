from django.db import models

from .utils import Currency, Language, Region


class Metacard(models.Model):
    public_id = models.CharField(max_length=255)
    is_delinquent = models.BooleanField()
    uid = models.CharField(max_length=45)
    currency = models.ForeignKey(Currency, models.DO_NOTHING)
    region = models.ForeignKey(Region, models.DO_NOTHING)
    language = models.ForeignKey(Language, models.DO_NOTHING)


class Contact(models.Model):
    email = models.CharField(max_length=70)
    provider = models.CharField(max_length=45, blank=True, null=True)
    public_id = models.CharField(max_length=255)
    is_active = models.BooleanField()
    created = models.DateTimeField()
