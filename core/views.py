from rest_framework.viewsets import ModelViewSet
from .models import Book, Author, Reader
from .serializers import AuthorSerializer, ReaderSerializer, BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


##############################  AUTHORS  ##############################

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


##############################  READERS  ##############################

class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

