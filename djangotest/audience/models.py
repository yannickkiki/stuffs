from django.db import models


class Audience(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "audience"
