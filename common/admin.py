from django.contrib import admin

from .models import SavedRequest


@admin.register(SavedRequest)
class SavedRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'path_info', 'request_method', 'created_dt')
