from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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

    def validate(self, attrs):
        if len(attrs['book_list']) > 3:
            raise serializers.ValidationError('На руках у читателя не может быть больше трех книг!')
        return attrs

    def create(self, validated_data):
        reader = super().create(validated_data)
        reader.set_password(reader.password)
        reader.save()

        book_list = validated_data.pop('book_list', [])
        for book in book_list:
            book.book_num -= 1
            book.save()
            reader.book_list.add(book)
        return reader

    def update(self, instance, validated_data):
        # Уменьшить количество книг в библиотеке, увеличить у читателя
        if validated_data['book_list']:
            for book in validated_data['book_list']:
                if book not in instance.book_list.all():
                    if book.book_num > 0:
                        book.book_num -= 1
                        book.save()
                    # Если нет книг в библиотеке, то сообщить об ошибке
                    else:
                        raise ValidationError(f'Книга "{book.name}", которую вы хотите добавить, на данный момент отсутствует в библиотеке.')
            # Увеличить количество книг в библиотеке, уменьшить у читателя
            for book in instance.book_list.all():
                if book not in validated_data['book_list']:
                    book.book_num += 1
                    book.save()

        return super().update(instance, validated_data)

    class Meta:
        model = Reader
        fields = "__all__"


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
            raise serializers.ValidationError("У книги не может быть отрицательное число страниц.")


class BookNumValidator:
    def __call__(self, value):
        if value < 0:
            raise serializers.ValidationError('Книг не может быть меньше нуля.')


class BookSerializer(serializers.ModelSerializer):
    pages = serializers.IntegerField(validators=[PagesCountValidator()])
    book_num = serializers.IntegerField(validators=[BookNumValidator()])

    class Meta:
        model = Book
        fields = "__all__"
