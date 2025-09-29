from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import CountryModel


@receiver(post_save, sender=CountryModel)
def CountrySignal(sender, instance, created, **kwargs): ...
