from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import CalendareventModel


@register(CalendareventModel)
class CalendareventTranslation(TranslationOptions):
    fields = []
