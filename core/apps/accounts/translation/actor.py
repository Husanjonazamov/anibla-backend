from modeltranslation.translator import TranslationOptions, register

from core.apps.accounts.models import ActorprofileModel


@register(ActorprofileModel)
class ActorprofileTranslation(TranslationOptions):
    fields = []
