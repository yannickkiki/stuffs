from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from subscription.models import StripeCustomer
from user.models import User

import stripe


class CsrfExemptMixin:

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        try:
            stripe_customer = StripeCustomer.objects.get(user=self.request.user)
        except StripeCustomer.DoesNotExist:
            return {}

        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_subscription = stripe.Subscription.retrieve(stripe_customer.stripe_subscription_id)
        stripe_product = stripe.Product.retrieve(stripe_subscription.plan.product)

        return {
            'subscription': stripe_subscription,
            'product': stripe_product,
        }


class StripeConfigView(CsrfExemptMixin, View):

    @staticmethod
    def get(request):
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


class CreateCheckoutSessionView(CsrfExemptMixin, View):

    @staticmethod
    def get(request):
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
        except Exception as e:
            return JsonResponse({'error': str(e)})
        else:
            return JsonResponse({'sessionId': checkout_session['id']})


class SuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'success.html'


class CancelView(LoginRequiredMixin, TemplateView):
    template_name = 'cancel.html'


class StripeWebhookView(CsrfExemptMixin, View):

    @staticmethod
    def post(request):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError:
            # Invalid signature
            return HttpResponse(status=400)

        # Handle the checkout.session.completed event
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']

            # Fetch all the required data from session
            client_reference_id = session.get('client_reference_id')
            stripe_customer_id = session.get('customer')
            stripe_subscription_id = session.get('subscription')

            # Get the user and create a new StripeCustomer
            user = User.objects.get(id=client_reference_id)
            StripeCustomer.objects.create(
                user=user,
                stripe_customer_id=stripe_customer_id,
                stripe_subscription_id=stripe_subscription_id,
            )
            print(user.username + ' just subscribed.')

        return HttpResponse(status=200)
