from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Book, Author, Reader
from .serializers import AuthorSerializer, ReaderSerializer, BookSerializer
from .permissions import PermissionPolicyMixin, PermissionAdminOrOwner


class BookViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
        'retrieve': [IsAdminUser]
    }


##############################  AUTHORS  ##############################

class AuthorViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
        'retrieve': [IsAdminUser]
    }


##############################  READERS  ##############################

class ReaderViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes_per_method = {
        'list': [PermissionAdminOrOwner],
        'create': [AllowAny],
        'update': [PermissionAdminOrOwner],
        'destroy': [PermissionAdminOrOwner],
        'retrieve': [PermissionAdminOrOwner]
    }

