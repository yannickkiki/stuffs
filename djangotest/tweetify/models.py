from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
