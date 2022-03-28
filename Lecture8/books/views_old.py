import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer


@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, safe=False, status=400)


@csrf_exempt
def book_detail(request, pk):
    book = Book.objects.filter(id=pk).first()
    if book:
        if request.method == 'GET':
            return JsonResponse(book.to_json_detail())
        elif request.method == 'PUT':
            data = json.loads(request.body)
            book.title = data.get('title', book.title)
            book.num_pages = data.get('num_pages', book.num_pages)
            book.publication_date = data.get('publication_date', book.publication_date)
            book.save()
            return JsonResponse(book.to_json_detail())
        elif request.method == 'DELETE':
            book.delete()
            return JsonResponse('', safe=False, status=204)
    return JsonResponse({'message': 'Book not found'}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class BookListView(ListView, CreateView):
    model = Book

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        data = [book.to_json() for book in books]
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        book = Book.objects.create(**data)
        # book = Book()
        # book.title = data['title']
        # book.num_pages = data['num_pages']
        # book.publication_date = data['publication_date']
        # book.save()
        return JsonResponse(book.to_json_detail())


@method_decorator(csrf_exempt, name='dispatch')
class BookDetailView(DetailView, UpdateView, DeleteView):
    model = Book

    def get(self, request, *args, **kwargs):
        book = Book.objects.filter(id=kwargs.get('pk')).first()
        if book:
            return JsonResponse(book.to_json_detail())
        return JsonResponse({'message': 'Book not found'}, status=404)

    def put(self, *args, **kwargs):
        book = Book.objects.filter(id=kwargs.get('pk')).first()
        if book:
            data = json.loads(self.request.body)
            book.title = data.get('title', book.title)
            book.num_pages = data.get('num_pages', book.num_pages)
            book.publication_date = data.get('publication_date', book.publication_date)
            book.save()
            return JsonResponse(book.to_json_detail())
        return JsonResponse({'message': 'Book not found'}, status=404)

    def delete(self, request, *args, **kwargs):
        book = Book.objects.filter(id=kwargs.get('pk')).first()
        if book:
            book.delete()
            return JsonResponse('', safe=False, status=204)
        return JsonResponse({'message': 'Book not found'}, status=404)
