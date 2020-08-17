from django.urls import path, reverse
from Books.views import BookListView, BookDetailView, BookSearchView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('search/', BookSearchView.as_view(), name='search')

]