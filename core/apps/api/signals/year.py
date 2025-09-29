from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import YearModel


@receiver(post_save, sender=YearModel)
def YearSignal(sender, instance, created, **kwargs): ...
