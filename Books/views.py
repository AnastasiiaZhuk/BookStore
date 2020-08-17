from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from Books.models import Book


class BookListView(LoginRequiredMixin, ListView):

    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    permission_required = 'Books.special_status'
    login_url = 'account_login'


class BookSearchView(ListView):

    model = Book
    template_name = 'books/search.html'
    context_object_name = 'book_list'

    def get_queryset(self):

        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
