from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('', include(('platify.urls', 'platify'), namespace='platify')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
