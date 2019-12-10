from django.urls import path

from . import views

urlpatterns = [
    path('', views.DocumentCreateView.as_view(), name='create'),
    path('private/', views.PrivateDocumentCreateView.as_view(), name='create_private')
]
