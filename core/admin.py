from django.contrib import admin
from .models import Reader, Author, Book


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "phone", "status",
                    "created", "edited")
    list_filter = ("name", "surname", "phone")
    list_display_links = ("name", "surname", "phone", "status")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "created", "edited")
    list_filter = ("name", "surname")
    list_display_links = ("name", "surname")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "pages", "book_num")
    list_filter = ("name", "description", "author")
    list_display_links = ("name", "description", "pages")
