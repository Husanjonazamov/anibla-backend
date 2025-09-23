from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import CalendareventModel


@admin.register(CalendareventModel)
class CalendareventAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
