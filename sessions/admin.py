from django.contrib import admin
from .models import Session


@admin.register(Session)
class GameAdmin(admin.ModelAdmin):
    list_display = ('map', 'number_of_teams')
