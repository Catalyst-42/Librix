from django.views.generic import TemplateView

from catalog.models import Book


class HomePage(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = Book.objects.count()

        return context
