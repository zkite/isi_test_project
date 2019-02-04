from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    USER_TYPE = [("ADMIN", "Admin"), ("DRIVER", "Driver")]

    username = models.CharField(
        max_length=150, unique=True, error_messages={'unique': _("A user with that username already exists.")}
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    user_type = models.CharField(max_length=150, choices=USER_TYPE, default="DRIVER")

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
