from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import YearModel


@admin.register(YearModel)
class YearAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
