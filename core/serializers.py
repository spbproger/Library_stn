from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Book, Author, Reader


class ReaderSerializer(serializers.ModelSerializer):
    phone = serializers.IntegerField(
        validators=[RegexValidator(r'^(?:\+79)\d{9,10}$',
                                   message="Phone number must be entered in the format: "
                                           "'+79998887766'. Up to 11 digits allowed.")])
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

    def validate_author(self, value):
        """
        Проверка условия, что указан автор/ы книги
        """
        if not value:
            raise serializers.ValidationError("Укажите автора/ов книги")
        return value

    class Meta:
        model = Book
        fields = "__all__"
