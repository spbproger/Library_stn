from django.contrib import admin

from .models import Reader, Author, Book

admin.site.register(Reader)
admin.site.register(Author)
admin.site.register(Book)