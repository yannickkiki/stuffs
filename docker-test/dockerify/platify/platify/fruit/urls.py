from django.urls import path

from .views import RegisterView, ProduceView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('produce/', ProduceView.as_view(), name='produce'),
]
