from django.db import models

# from segment.models import Segment as Audience
from audience.models import Audience


class Campaign(models.Model):
    audience = models.ForeignKey(Audience, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    namo = models.CharField(max_length=255)

    class Meta:
        db_table = "campaign"
