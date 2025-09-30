from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from core.apps.api.models import AnimeModel


@admin.register(AnimeModel)
class AnimeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "title",
    )
    search_fields = ("title", ) 
