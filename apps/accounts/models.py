from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), blank=False, unique=True)
    is_admin = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

    def set_email(self, email):
        self.email = email
