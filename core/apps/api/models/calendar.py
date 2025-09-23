from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CalendareventModel(AbstractBaseModel):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField()
    date = models.DateField()
    created_by = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True, related_name="created_events")

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "CalendarEvent"
        verbose_name = _("CalendareventModel")
        verbose_name_plural = _("CalendareventModels")
