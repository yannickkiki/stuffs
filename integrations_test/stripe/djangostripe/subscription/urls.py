from django.urls import path
from .views import HomeView, StripeConfigView, CreateCheckoutSessionView, SuccessView, CancelView, StripeWebhookView

urlpatterns = [
    path('', HomeView.as_view(), name='subscriptions-home'),
    path('config/', StripeConfigView.as_view()),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view()),
    path('success/', SuccessView.as_view()),
    path('cancel/', CancelView.as_view()),
    path('webhook/', StripeWebhookView.as_view())
]
