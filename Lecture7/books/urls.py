from django.urls import path
from books.views import book_list, book_detail, BookListView, BookDetailView

urlpatterns = [
    # path('', book_list),
    # path('<int:pk>/', book_detail)
    path('', BookListView.as_view()),
    path('<int:pk>/', BookDetailView.as_view())
]
