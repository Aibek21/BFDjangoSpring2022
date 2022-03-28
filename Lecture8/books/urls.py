from django.urls import path
from books.views import book_list, BookListAPIView, BookAPIView, BookDetailApiView

urlpatterns = [
    # path('', book_list),
    # path('<int:pk>/', book_detail)
    # path('', BookListView.as_view()),
    # path('<int:pk>/', BookDetailView.as_view())
    # path('', BookListAPIView.as_view())
    path('', BookAPIView.as_view()),
    path('<int:pk>/', BookDetailApiView.as_view())
]
