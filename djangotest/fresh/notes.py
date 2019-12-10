from django.db.models import FilteredRelation, Q

from .models import Account

# Select accounts that are not related to queue items with templet_id = 2
Account.objects.exclude(queue__templet_id=2)  # use IN

Account.objects.annotate(queue_current_templet=FilteredRelation('queue', condition=Q(queue__templet_id=2)))\
    .filter(queue_current_templet=None)  # use LEFT JOIN


# How to "join" through a field that is not foreign key in Django:

# 1 - set the field as models.ForeignKey but with db_constraint=False and use django lookups as usual

# 2 - get the data you need from the other tables in subqueries
from fresh.models import Product, ProductCategory
from django.db.models import Subquery, OuterRef
products = Product.objects.annotate(category_name=Subquery(
    ProductCategory.objects.filter(id=OuterRef('category_id')).values('name')[:1]
))
#   or
products = Product.objects.extra(
    select={
        'category_name': 'SELECT fresh_productcategory.name FROM fresh_productcategory '
                         'WHERE fresh_product.category_id=fresh_productcategory.id'
    }
)
