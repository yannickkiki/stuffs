from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('amaz.urls', 'amaz'), namespace='amaz')),
]
