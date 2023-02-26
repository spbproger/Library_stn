# from rest_framework.utils import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.generics import get_object_or_404
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Book, Author, Reader
from .serializers import AuthorSerializer, ReaderSerializer, BookNewSerializer


##############################  BOOKS  ##############################
# ListAPIView for Books
@csrf_exempt
def all_books(request):
    if request.method == "GET":
        query = Book.objects.all()

        response = BookNewSerializer(query, many=True).data

        return JsonResponse(data=response, safe=False)
    elif request.method == "POST":
        return JsonResponse({'error': 'method not allowed'})


# RetrieveAPIView for Books
@csrf_exempt
def one_book(request, book_id):
    if request.method == "GET":
        try:
            query = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'item not exist'})

        response = BookNewSerializer(query).data

        return JsonResponse(data=response, safe=False)
    elif request.method == "POST":
        return JsonResponse({'error': 'method not allowed'})


# CreateAPIView for Books
class CreateBook(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookNewSerializer


# UpdateAPIView for Books
class UpdateBook(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookNewSerializer


# DestroyAPIView for Books
class DeleteBook(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookNewSerializer


##############################  AUTHORS  ##############################

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


##############################  READERS  ##############################

class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

