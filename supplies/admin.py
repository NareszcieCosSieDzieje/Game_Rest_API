from django.contrib import admin
from .models import Supply


@admin.register(Supply)
class GameAdmin(admin.ModelAdmin):
    list_display = ('duration', ) # map
