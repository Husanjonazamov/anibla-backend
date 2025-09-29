from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import AnimeModel


@receiver(post_save, sender=AnimeModel)
def AnimeSignal(sender, instance, created, **kwargs): ...
