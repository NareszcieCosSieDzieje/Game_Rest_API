from django.contrib import admin
from .models import Map


@admin.register(Map)
class GameAdmin(admin.ModelAdmin):
    list_display = ('max_players', )

