from django.contrib.auth.models import User  # type: ignore[reportMissingModuleSource]
from django.db import models  # type: ignore[reportMissingModuleSource]


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="account_profile"
    )

    bio = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )