from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Book

class BookListView(ListView):
    model = Book
    ordering = 'id'
    paginate_by = 10

    def get_context_data(self,**kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search') or ''
        context['search'] = search

        return context

    def get_queryset(self):
        query = self.request.GET.get('search') or ''

        if query:
            object_list = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__second_name__icontains=query) |
                Q(author__last_name__icontains=query)
            )
        else:
            object_list = self.model.objects.all()

        return object_list


class BookDetailView(DetailView):
    model = Book
