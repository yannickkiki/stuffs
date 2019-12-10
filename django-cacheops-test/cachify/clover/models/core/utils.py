from django.db import models


class Currency(models.Model):
    iso = models.CharField(max_length=3)
    name = models.CharField(max_length=45)


class Region(models.Model):
    name = models.CharField(max_length=45)
    power = models.IntegerField()


class Language(models.Model):
    iso = models.CharField(max_length=2)
    name = models.CharField(max_length=255)
