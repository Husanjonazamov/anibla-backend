from modeltranslation.translator import TranslationOptions, register

from core.apps.accounts.models import DirectorModel


@register(DirectorModel)
class DirectorTranslation(TranslationOptions):
    fields = []
