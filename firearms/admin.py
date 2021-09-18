from django.contrib import admin
from .models import Firearm


@admin.register(Firearm)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'fire_rate', 'clip_capacity', 'clip_cartridges',
                    'damage', 'ammunition_type')

