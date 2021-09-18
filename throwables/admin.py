from django.contrib import admin
from .models import Throwable


@admin.register(Throwable)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'size', 'throw_range', 'damage')
