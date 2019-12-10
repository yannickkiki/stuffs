from django.db import models

from .metacard import MetaCard
from .trellis_card import TrellisCard


class Product(models.Model):
    price_min = models.DecimalField(max_digits=17, decimal_places=4, null=True)
    created = models.DateTimeField(null=False)
    last_suggested = models.DateTimeField(null=True)
    image = models.ImageField()
    variants_count = models.IntegerField(default=0)
    metacard = models.OneToOneField(MetaCard, related_name='product', on_delete=models.CASCADE, null=True)
    trellis_card = models.OneToOneField(TrellisCard, related_name='product', on_delete=models.CASCADE, null=True)


Product.objects.all()
