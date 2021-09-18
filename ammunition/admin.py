from django.contrib import admin
from .models import Ammunition


@admin.register(Ammunition)
class GameAdmin(admin.ModelAdmin):
    list_display = ('caliber', 'caliber_type')
