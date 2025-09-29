from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleChoice(models.TextChoices):
    """
    Foydalanuvchi rollari
    """
    ADMIN = "admin", _("Direktor")    
    MANAGER = "manager", _("Manager")
    DIRECTOR = "director", _("Rejisyor")  
    ACTOR = "actor", _("Aktyor")


class GenderChoice(models.TextChoices):
    MALE = "male", _("Erkak")
    FEMALE = "FEMALE", _("Ayol")
    
    
    