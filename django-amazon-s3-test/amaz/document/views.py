from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Document, PrivateDocument


class DocumentCreateView(CreateView):
    model = Document
    fields = ['file']
    success_url = reverse_lazy('amaz:document:create')

    def form_valid(self, form):
        print(f"\n\n{form.cleaned_data}\n\n")
        return super().form_valid(form=form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = self.model.objects.all()
        return context


class PrivateDocumentCreateView(DocumentCreateView):
    model = PrivateDocument
    success_url = reverse_lazy('amaz:document:create_private')
