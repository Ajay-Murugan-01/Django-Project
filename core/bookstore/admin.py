from django.contrib import admin

# Register your models here.
from . models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price', 'publish_date']

admin.site.register(Book, BookAdmin)