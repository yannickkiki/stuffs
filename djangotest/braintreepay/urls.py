from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('client-token', views.ClientTokenView.as_view(), name='client_token'),
    path('checkout', views.CheckoutView.as_view(), name='checkout'),
]
