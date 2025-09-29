from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CalendareventModel(AbstractBaseModel):
    anime = models.ForeignKey("api.AnimeModel", on_delete=models.CASCADE)
    director = models.ForeignKey("accounts.DirectorModel", on_delete=models.CASCADE)
    actors = models.ManyToManyField("accounts.ActorprofileModel", related_name="actors", blank=True, null=True)
    record_date = models.DateField()


    def __str__(self):
        return f"{self.anime.title}-{self.record_date}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "CalendarEvent"
        verbose_name = _("CalendareventModel")
        verbose_name_plural = _("CalendareventModels")
