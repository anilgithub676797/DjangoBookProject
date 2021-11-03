from django.contrib import admin
from book_application.models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'published_date']


admin.site.register(Book, BookAdmin)
