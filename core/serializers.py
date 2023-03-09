from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Book, Author, Reader


class ReaderSerializer(serializers.ModelSerializer):
    # Валидатором номера телефона выступает валидатор регулярных выражений
    phone = serializers.IntegerField(
        validators=[RegexValidator(r'^[7]\d{10}$',
                                   message="Формат номера должен иметь вид "
                                           "79998887766, и состоять из 11 цифр.")])
    book_list = serializers.SlugRelatedField(queryset=Book.objects.all(),
                                             slug_field="name",
                                             many=True
                                             )

    class Meta:
        model = Reader
        fields = "__all__"

    def validate(self, data):
        book_list = data.get('book_list')
        for book in book_list:
            if book.book_num == 0:
                raise serializers.ValidationError(f"Книгу '{book.name}' добавить невозможно. Нет в наличии.")
            return data

    def create(self, validated_data):
        book_list = validated_data.pop('book_list', [])
        reader = super().create(validated_data)
        for book in book_list:
            book.book_num -= 1
            book.save()
            reader.book_list.add(book)
        return reader

    def update(self, instance, validated_data):
        books = validated_data.pop('book_list', [])
        reader = super().update(instance, validated_data)

        # Получение множеств книг
        new_list_books = set(books)
        old_list_books = set(instance.book_list.all())

        # Обновление количества каждой книги
        for book in old_list_books - new_list_books:
            book.book_num += 1
            book.save()

        for book in new_list_books - old_list_books:
            book.book_num -= 1
            book.save()

        # Добавление новой книги
        for book in new_list_books - old_list_books:
            instance.book_list.add(book)

        # Удаление старой книги
        for book in old_list_books - new_list_books:
            instance.book_list.remove(book)

        return reader


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


# Проверка неотрицательного значения количества книг и страниц в них
# Однако, такая валидация может выполняться типом поля PositiveSmallIntegerField
# без дополнительных валидаторов
class PagesCountValidator:
    def __call__(self, value):
        if value < 0:
            raise serializers.ValidationError("У книги не может быть отрицательное число страниц")


class BookSerializer(serializers.ModelSerializer):
    pages = serializers.IntegerField(validators=[PagesCountValidator()])

    class Meta:
        model = Book
        fields = "__all__"
