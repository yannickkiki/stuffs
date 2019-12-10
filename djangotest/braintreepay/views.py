from django.http import JsonResponse
from django.views.generic import TemplateView

from rest_framework.views import APIView

import braintree


gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="w223v5zd43njjwjp",
        public_key="dvdndmb7d59yvpjk",
        private_key="52450b7b9c46ceae0574c6e0d65e2717"
    )
)


class IndexView(TemplateView):
    template_name = 'braintreepay/index.html'


class ClientTokenView(APIView):

    def get(self, request, *args, **kwargs):
        # client_token = gateway.client_token.generate({
        #     "customer_id": a_customer_id
        # }) # add `customer_id` can help autofill past informations
        client_token = gateway.client_token.generate()
        return JsonResponse(data={'token': client_token})


class CheckoutView(APIView):

    def post(self, request, *args, **kwargs):
        nonce_from_the_client = request.data["payment_method_nonce"]
        # device_data_from_the_client = request.data["device_data"] # todo: review advanced fraud stuff
        result = gateway.transaction.sale({
            "amount": "18.50",
            "payment_method_nonce": nonce_from_the_client,
            "options": {
                "submit_for_settlement": True
            }
        })

        # # Show transaction
        # transaction = gateway.transaction.find(result.transaction.id)
        # result = {}
        # TRANSACTION_SUCCESS_STATUSES = [
        #     braintree.Transaction.Status.Authorized,
        #     braintree.Transaction.Status.Authorizing,
        #     braintree.Transaction.Status.Settled,
        #     braintree.Transaction.Status.SettlementConfirmed,
        #     braintree.Transaction.Status.SettlementPending,
        #     braintree.Transaction.Status.Settling,
        #     braintree.Transaction.Status.SubmittedForSettlement
        # ]
        # if transaction.status in TRANSACTION_SUCCESS_STATUSES:
        #     result = {
        #         'header': 'Sweet Success!',
        #         'icon': 'success',
        #         'message': 'Your test transaction has been successfully processed. '
        #                    'See the Braintree API response and try again.'
        #     }
        # else:
        #     result = {
        #         'header': 'Transaction Failed',
        #         'icon': 'fail',
        #         'message': 'Your test transaction has a status of '
        #                    '' + transaction.status + '. See the Braintree API response and try again.'
        #     }
        return JsonResponse(data={'success': result.is_success})
