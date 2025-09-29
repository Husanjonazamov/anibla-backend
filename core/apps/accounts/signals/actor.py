from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.accounts.models import ActorprofileModel


@receiver(post_save, sender=ActorprofileModel)
def ActorprofileSignal(sender, instance, created, **kwargs): ...
