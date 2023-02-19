from django.db import models


class Reader(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.BigIntegerField(verbose_name="Номер телефона")
    status = models.BooleanField(default=True, verbose_name="Активен")
    book_list = models.ManyToManyField("Book", blank=True, related_name="books", verbose_name="Список книг")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    photo = models.ImageField(upload_to="media/%Y/%m/%d/", null=True, blank=True, verbose_name="Фото")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    pages = models.PositiveSmallIntegerField(verbose_name="Количество страниц")
    author = models.ManyToManyField(Author, related_name="authors", verbose_name="Авторы")
    book_num = models.PositiveIntegerField(verbose_name="Количество книг")

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('-name', )

    def __str__(self):
        return self.name
