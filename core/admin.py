from django.contrib import admin
from django.db.models import QuerySet

from .models import Reader, Author, Book


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ("surname", "name", "books_count", "phone", "status",
                    "created", "edited")
    list_filter = ("status",)
    list_display_links = ("name", "surname", "phone", "status")

    fieldsets = (
        (None, {
            "fields": ("surname", "name")
        }),
        ("Книги на руках", {
            "fields": ("book_list",)
        }),
        ("Дополнительные сведения", {
            "fields": ("phone", "status")
        }),
    )

    actions = ("change_false_status", "change_true_status", "clear_booklist")

    @admin.action(description='Изменить статус: Неактивный')
    def change_false_status(self, request, queryset: QuerySet):
        """
        Экшн изменения статуса читателя на Неактивного
        """
        queryset.update(status=False)
        self.message_user(request, f'Статус читателя изменен на "Неактивный"')

    @admin.action(description='Изменить статус: Активный')
    def change_true_status(self, request, queryset: QuerySet):
        """
        Экшн изменения статуса читателя на Активного
        """
        queryset.update(status=True)
        self.message_user(request, f'Статус читателя изменен на "Активный"')

    @admin.action(description='Очистить список книг')
    def clear_booklist(self, request, queryset: QuerySet):
        """
        Экшн очистки списка книг на руках у читателя
        """
        queryset.update(book_list=[])
        count = queryset.get().pk
        self.message_user(request, f'Количество книг на руках у читателя: {count}')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("surname", "name", "created", "edited")
    list_filter = ("name", "surname")
    list_display_links = ("name", "surname")
    search_fields = ("surname",)

    fieldsets = (
        (None, {
            "fields": ("surname", "name")
        }),
        ("Медиафайлы", {
            "fields": ("photo",)
        }),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "author_link", "description", "pages", "book_num")
    list_filter = ("author",)
    list_display_links = ("name", "description")
    search_fields = ("author",)

    fieldsets = (
        (None, {
            "fields": ("name", "description", "pages", "book_num")
        }),
        ("Укажите автора/ов", {
            "fields": ("author",)
        }),
    )
