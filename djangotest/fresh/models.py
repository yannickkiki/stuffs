from django.db import models


class StrMixin:

    def __str__(self):
        return str({key: value for key, value in self.__dict__.items() if not key.startswith('_')})


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.IntegerField()  # foreign key referencing ProductCategory
    is_active = models.BooleanField(default=False)


class ProductSettings(models.Model):
    description = models.CharField(max_length=255)
    product_id = models.IntegerField()  # one to one referencing Product


class Account(StrMixin, models.Model):
    is_active = models.BooleanField(default=True)


class Queue(StrMixin, models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    templet_id = models.IntegerField(default=1)

    def __str__(self):
        return str({key: value for key, value in self.__dict__.items() if not key.startswith('_')})


class History(StrMixin, models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    templet_id = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
