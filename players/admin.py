from django.contrib import admin
from .models import Player


@admin.register(Player)
class GameAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'team_id',
                    'inventory_size', 'inventory_weight')
