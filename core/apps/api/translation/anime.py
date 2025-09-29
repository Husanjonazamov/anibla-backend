from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import AnimeModel


@register(AnimeModel)
class AnimeTranslation(TranslationOptions):
    fields = [
        "title",
        "description",
    ]
