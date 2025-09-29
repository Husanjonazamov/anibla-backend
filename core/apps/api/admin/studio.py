from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from core.apps.api.models import StudioModel


@admin.register(StudioModel)
class StudioAdmin(ModelAdmin,TabbedTranslationAdmin):
    list_display = (
        "id",
        "__str__",
    )
