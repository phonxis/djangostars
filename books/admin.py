from django.contrib import admin

from .models import Book, LogBookAction


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'price', 'created_dt')
    search_fields = ('title', 'isbn')


@admin.register(LogBookAction)
class LogBookActionAdmin(admin.ModelAdmin):
    list_display = ('action_type', 'user', 'created_dt')
