from django.urls import include, path

from rest_framework import routers

from .product.viewsets import ProductViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)


urlpatterns = [
    path('api/', include((router.urls, 'api'), namespace='api')),

    path('fruit/', include(('platify.fruit.urls', 'platify.fruit'), namespace='fruit')),
    path('upload/', include(('platify.upload.urls', 'platify.upload'), namespace='upload')),
]
