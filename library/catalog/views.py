from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Book

class BookListView(ListView):
    model = Book
    ordering = 'id'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search') or ''
        context['search'] = search
        context['search_by_title'] = self.request.GET.get('search_by_title') == 'on'
        context['search_by_author'] = self.request.GET.get('search_by_author') == 'on'
        context['search_by_genre'] = self.request.GET.get('search_by_genre') == 'on'

        if search == '' or (
                not context['search_by_title'] and
                not context['search_by_author'] and
                not context['search_by_genre']
            ):
            context['search_by_title'] = True
            context['search_by_author'] = True

        return context

    def get_queryset(self):
        query = self.request.GET.get('search') or ''
        search_by_title = self.request.GET.get('search_by_title') == 'on'
        search_by_author = self.request.GET.get('search_by_author') == 'on'
        search_by_genre = self.request.GET.get('search_by_genre') == 'on'

        filters = Q()

        if query and search_by_title:
            filters |= Q(title__icontains=query)

        if query and search_by_author:
            filters |= (
                Q(author__first_name__icontains=query) |
                Q(author__second_name__icontains=query) |
                Q(author__last_name__icontains=query)
            )

        if query and search_by_genre:
            filters |= Q(genre__genre__icontains=query)

        if filters:
            return self.model.objects.filter(filters)
        else:
            return self.model.objects.all()


class BookDetailView(DetailView):
    model = Book
