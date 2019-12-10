from django.db import models
from django.utils.functional import cached_property

from .core.utils import Currency, Region, Language

from caching.base import CachingManager, CachingMixin


class Clover(CachingMixin, models.Model):
    """
    Clover is an optimization table with only purpose of helping speed up the application
    and avoid unnecessary queries. All information accessible in clover are retrieved from other tables.
    Performing the same select multiple time on clover is okay as clover use cache to retrieve its result instead of db
    Because clover is heavily optimized and handle its own cache, here are a few recommendations when using clover.

    - Default to using clover versus metacard, card, shop, or lattice when applicable
    - Do not use `select_related` using clover, this may not always give expected result.
    - Do not add any foreignkey on another model pointing to clover,
    - Do not subclass or inherit clover even if it is a proxy model
    - Do not attempt to edit or update any value in clover
    - Do not perform any aggregate on clover
    - Do not use `count`, `values`, `values_list` on clover
    - Do not use `only` on clover to only selected some fields, it will be counter-productive because of caching

    example:
    The following example will not perform any db query.
    clover = Clover.objects.get(shop_id=X)
    if not clover.foxx_is_active:
        return

    """

    # never change
    shop_id = models.IntegerField(unique=True)
    ctype = models.CharField(max_length=45)
    card_id = models.IntegerField(unique=True, null=True)
    card_pid = models.CharField(max_length=45, unique=True, null=True)  # card.public_id
    card_uid = models.CharField(max_length=45, unique=True, null=True)
    lattice_id = models.IntegerField(unique=True, null=True)

    # rarely change
    shop_handle = models.CharField(max_length=255, unique=True)
    region = models.ForeignKey(Region, null=True, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, null=True, on_delete=models.PROTECT)
    currency = models.ForeignKey(Currency, null=True, on_delete=models.PROTECT)

    # can be updated frequently
    is_arrow_active = models.BooleanField(null=True)
    is_bamboo_active = models.BooleanField(null=True)
    is_foxx_active = models.BooleanField(null=True)
    is_liana_active = models.BooleanField(null=True)
    is_lotus_active = models.BooleanField(null=True)
    is_poppy_active = models.BooleanField(null=True)
    is_snow_active = models.BooleanField(null=True)
    is_ultimate_active = models.BooleanField(null=True)

    objects = CachingManager()

    def __str__(self):
        return str(self.shop_handle)

    @cached_property
    def shop(self):
        from clover.models.radix import Shop
        shop = Shop.objects.get(id=self.shop_id)
        return shop

    @cached_property
    def metacard(self):
        if not self.card_id:
            return None
        from clover.models.core import Metacard
        return Metacard.objects.get(id=self.card_id)

    def get_card(self, itype):
        return getattr(self.metacard, itype)
