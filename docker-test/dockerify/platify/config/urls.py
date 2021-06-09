from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin





urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('upload/', include(('platify.upload.urls', 'upload'), namespace='upload')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
