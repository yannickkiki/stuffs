from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('critical', views.CriticalLogView.as_view(), name='critical'),
    path('warning', views.WarningLogView.as_view(), name='warning'),
]
