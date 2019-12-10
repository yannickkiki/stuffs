from django.urls import include, path

urlpatterns = [
    path('fruit/', include(('proj.fruit.urls', 'proj.fruit'), namespace='fruit')),
]
