from modeltranslation.translator import TranslationOptions, register

from core.apps.accounts.models import ManagerModel


@register(ManagerModel)
class ManagerTranslation(TranslationOptions):
    fields = []
