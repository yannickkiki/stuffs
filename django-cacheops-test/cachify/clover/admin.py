from django.contrib import admin

from .models import Clover
from .models.core import Metacard, Contact, Currency, Language, Region
from .models.radix import Shop

admin.site.register(Clover)

admin.site.register(Metacard)
admin.site.register(Contact)
admin.site.register(Currency)
admin.site.register(Language)
admin.site.register(Region)

admin.site.register(Shop)
