from django.db import models  # type: ignore[import-not-found]
from django.contrib.auth.models import User  # type: ignore[import-not-found]


class Diagnosis(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    image = models.ImageField(
        upload_to="diagnostics/"
    )


    plant_name = models.CharField(
        max_length=150
    )


    disease = models.CharField(
        max_length=150,
        blank=True
    )


    confidence = models.FloatField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )