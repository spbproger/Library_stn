from django.db import models
from django.urls import reverse
from django.utils.html import format_html


class Reader(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.BigIntegerField(verbose_name="Номер телефона")
    status = models.BooleanField(default=True, verbose_name="Активен")
    book_list = models.ManyToManyField("Book", blank=True, related_name="books", verbose_name="Список книг")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited = models.DateTimeField(auto_now=True, verbose_name="Дата последнего редактирования")

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return self.name

    @property
    def fullname(self):
        """
        Определение метода объединения имени и фамилии как поля у модели Читателя
        """
        return f"{self.name} {self.surname}"

    def books_count(self):
        """
        Метод считает количество книг на руках у Читателя
        """
        count = self.book_list.count()
        return count

    books_count.short_description = "Количество книг на руках"


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    photo = models.ImageField(upload_to="media/%Y/%m/%d/", null=True, blank=True, verbose_name="Фото")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited = models.DateTimeField(auto_now=True, verbose_name="Дата последнего редактирования")

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ('surname', 'name')

    @property
    def fullname(self):
        """
        Определение метода объединения имени и фамилии как поля у модели Автора
        """
        return f"{self.name} {self.surname}"

    def __str__(self):
        return f'{self.fullname}'


class Book(models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    pages = models.PositiveSmallIntegerField(verbose_name="Количество страниц")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Авторы")
    book_num = models.PositiveIntegerField(verbose_name="Общее количество книг")

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('-name',)

    def __str__(self):
        return self.name

    def author_link(self):
        """
        Реализация ссылки (перехода) на страницу редактирования автора книги
        """
        author = self.author
        url = reverse("admin:core_author_changelist") + str(author.pk)
        return format_html(f'<a href="{url}">{author}</a>')

# При связи Многие-ко-Многим метод будет реализовывать вывод списка авторов книги в инфоокне о книгах
# def get_authors(self):
#     return "; ".join([author.name + " " + author.surname for author in self.author.all()])
# get_authors.short_description = "Авторы"
