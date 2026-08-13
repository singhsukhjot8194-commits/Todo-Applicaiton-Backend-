from django.contrib import admin
from .models import TODOO

@admin.register(TODOO)
class TODOOAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'user__username')
    readonly_fields = ('date',)
