from django.urls import path, include

urlpatterns = [
    path('', include(('amaz.core.urls', 'core'), namespace='core')),
    path('document/', include(('amaz.document.urls', 'document'), namespace='document')),
]
