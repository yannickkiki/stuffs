import logging

from django.db.models.fields.related_descriptors import ReverseOneToOneDescriptor
from django.views.generic import TemplateView
from django.db.migrations import AlterField


class CriticalLogView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        app_logger = logging.getLogger('app_logger')
        app_logger.critical("A critical event occurred")
        return super().get_context_data()


class WarningLogView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        app_logger = logging.getLogger('app_logger')
        app_logger.warning("A warning event occurred")
        return super().get_context_data()
