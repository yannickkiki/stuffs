from django.urls import include, path

from rest_framework import routers

from .product.viewsets import ProductViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)


urlpatterns = [
    path('fruit/', include(('platify.fruit.urls', 'platify.fruit'), namespace='fruit')),
]
