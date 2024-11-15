from django.views.generic import TemplateView

from catalog.models import Book, Author, Translator, Genre


class HomePage(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_books'] = Book.objects.count()
        context['total_authors'] = Author.objects.count()
        context['total_translators'] = Translator.objects.count()
        context['total_genres'] = Genre.objects.count()

        return context
