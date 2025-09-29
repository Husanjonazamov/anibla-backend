from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import StudioModel


@admin.register(StudioModel)
class StudioAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
