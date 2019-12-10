from django.contrib import admin
from django.urls import path, include

import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('debug/', include(debug_toolbar.urls)),
    path('user/', include('user.urls', namespace='user'))
]
