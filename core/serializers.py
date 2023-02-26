from rest_framework import serializers
from core.models import Book, Author, Reader


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    pages = serializers.IntegerField
    author = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='surname'
    )
    book_num = serializers.IntegerField()


class ReaderSerializer(serializers.ModelSerializer):
    book_list = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field="name", many=True)

    class Meta:
        model = Reader
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
