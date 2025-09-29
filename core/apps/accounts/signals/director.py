from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.accounts.models import DirectorModel


@receiver(post_save, sender=DirectorModel)
def DirectorSignal(sender, instance, created, **kwargs): ...
