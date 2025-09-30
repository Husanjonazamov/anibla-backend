from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from ..choices import RoleChoice, GenderChoice


class ActorprofileModel(AbstractBaseModel):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name=_("Yoshi"))
    gender = models.CharField(verbose_name=_("Jinsi"), choices=GenderChoice.choices, default=GenderChoice.MALE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatar/", default="avatar/logo.png")

    
    def __str__(self):
        return str(self.user.first_name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "ActorProfile"
        verbose_name = _("ActorprofileModel")
        verbose_name_plural = _("ActorprofileModels")
