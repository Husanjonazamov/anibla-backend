from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import StudioModel


@register(StudioModel)
class StudioTranslation(TranslationOptions):
    fields = []
