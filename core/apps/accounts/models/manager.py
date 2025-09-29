from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ManagerModel(AbstractBaseModel):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    age = models.IntegerField(default=22)
    avatar = models.ImageField(upload_to="manager/avatar/", default="avatar/logo.png")
    bio = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return str(self.user.first_name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "manager"
        verbose_name = _("ManagerModel")
        verbose_name_plural = _("ManagerModels")
