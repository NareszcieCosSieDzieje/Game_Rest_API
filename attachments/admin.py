from django.contrib import admin
from .models import Attachment


@admin.register(Attachment)
class GameAdmin(admin.ModelAdmin):
    list_display = ('type', )

