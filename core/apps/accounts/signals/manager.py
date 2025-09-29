from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.accounts.models import ManagerModel


@receiver(post_save, sender=ManagerModel)
def ManagerSignal(sender, instance, created, **kwargs): ...
