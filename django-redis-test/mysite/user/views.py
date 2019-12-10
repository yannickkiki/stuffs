from django.views.generic import TemplateView

from django.contrib.auth.models import User


class UserView(TemplateView):
    template_name = 'user/index.html'

    def get_context_data(self, **kwargs):
        context = {
            'users': User.objects.all()
        }
        return context
