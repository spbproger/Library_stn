from rest_framework import serializers
from core.models import Book, Author, Reader


class ReaderSerializer(serializers.ModelSerializer):
    book_list = serializers.SlugRelatedField(
        queryset=Book.objects.all(),
        slug_field="name",
        many=True)

    class Meta:
        model = Reader
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookNewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=Author.objects.all(),
        many=True,
        slug_field="surname"
    )

    class Meta:
        model = Book
        fields = "__all__"
