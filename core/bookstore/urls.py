from django.urls import path
from .views import BookCreateView, BookDetailView, BookUpdateView, BookDeleteView, BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:id>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:id>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
