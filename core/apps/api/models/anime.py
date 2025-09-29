from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class AnimeChoice(models.TextChoices):
    series = "series", _("Serial")
    movie = "movie", _("To'liq metraj")



class AnimeModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Nomi"), max_length=255)
    anime_type = models.CharField(max_length=15, choices=AnimeChoice.choices, default=AnimeChoice.movie)
    description = models.TextField(blank=True, null=True)
    episodes_count = models.PositiveIntegerField(default=1)
    country = models.ForeignKey("api.CountryModel", on_delete=models.SET_NULL, blank=True, null=True)
    year = models.ForeignKey("api.YearModel", on_delete=models.SET_NULL, blank=True, null=True)
    studio = models.ForeignKey("api.StudioModel", on_delete=models.SET_NULL, blank=True, null=True)
    
    manager = models.ForeignKey("accounts.ManagerModel", on_delete=models.CASCADE)
    director = models.ForeignKey("accounts.DirectorModel", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "anime"
        verbose_name = _("AnimeModel")
        verbose_name_plural = _("AnimeModels")
