from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import CountryModel


@register(CountryModel)
class CountryTranslation(TranslationOptions):
    fields = [
        "name"
    ]
