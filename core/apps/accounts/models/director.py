from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class DirectorModel(AbstractBaseModel):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    age = models.IntegerField(default=18)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="director-avatar/", default="avatar/logo.png")


    def __str__(self):
        return str(self.user.first_name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "director"
        verbose_name = _("DirectorModel")
        verbose_name_plural = _("DirectorModels")
