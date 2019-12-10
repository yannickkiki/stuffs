from django.db import models

from clover.models.core import Metacard, Contact


class Shop(models.Model):
    handle = models.CharField(max_length=255, unique=True, null=False)
    metacard = models.OneToOneField(Metacard, null=True, related_name='metashop', blank=True, on_delete=models.PROTECT)
    ctype = models.CharField(max_length=45, null=False)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=70, null=True, blank=True)
    shopname = models.CharField(max_length=255, null=True, blank=True)
