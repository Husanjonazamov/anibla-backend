from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import YearModel


@register(YearModel)
class YearTranslation(TranslationOptions):
    fields = []
