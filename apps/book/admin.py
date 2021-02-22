from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "modified")
    list_filter = ("created", "modified")
    filter_horizontal = ["authors"]
