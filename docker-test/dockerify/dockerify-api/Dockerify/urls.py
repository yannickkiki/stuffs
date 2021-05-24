from django.urls import include, path
from django.contrib import admin

from rest_framework import routers

from product.viewsets import ProductViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
