from django.contrib.auth.middleware import AuthenticationMiddleware

from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request


class YannickModelViewSet(ModelViewSet):

    def initialize_request(self, request, *args, **kwargs):
        super().initialize_request()
