from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import CalendareventModel


@admin.register(CalendareventModel)
class CalendareventAdmin(ModelAdmin):
    list_display = (
        "id",
    )
    
    autocomplete_fields = ["actors", "director", "anime", ]

