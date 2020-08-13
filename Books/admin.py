from django.contrib import admin
from Books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price",)


admin.site.register(Book, BookAdmin)
# Register your models here.
