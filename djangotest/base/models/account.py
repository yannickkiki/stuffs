from django.contrib.postgres.fields import ArrayField
from django.db import models
import django.db.backends.postgresql


class Account(models.Model):
    bounced = models.DateTimeField()
    bounced_list = ArrayField(models.DateTimeField(), default=list)


class ProductSuggestion(models.Model):
    account = models.IntegerField()
    scheduled = models.DateTimeField()
    customer_id_new = models.IntegerField()
