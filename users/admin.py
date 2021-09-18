from django.contrib import admin
from .models import User


@admin.register(User)
class GameAdmin(admin.ModelAdmin):
    list_display = ('username', 'ranking', 'score', 'played_matches')
