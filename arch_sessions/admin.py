from django.contrib import admin
from .models import ArchSession


@admin.register(ArchSession)
class GameAdmin(admin.ModelAdmin):
    list_display = ('serialized_map', 'serialized_players')
