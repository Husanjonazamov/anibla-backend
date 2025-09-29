from django.contrib.auth import models as auth_models
from django.db import models

from ..choices import RoleChoice, GenderChoice
from ..managers import UserManager



class User(auth_models.AbstractUser):
    phone = models.CharField(max_length=255, unique=True)
    tg_id = models.BigIntegerField(default=0)
    username = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    validated_at = models.DateTimeField(null=True, blank=True)
    role = models.CharField(
        max_length=255,
        choices=RoleChoice,
        default=RoleChoice.ACTOR,
    )

    USERNAME_FIELD = "phone"
    objects = UserManager()

    def __str__(self):
        return self.phone
