from django.db import models
from django.contrib.auth.models import User

from plants.models import Plant



class Identification(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    plant = models.ForeignKey(
        Plant,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )


    image = models.ImageField(
        upload_to="identifications/"
    )


    confidence = models.FloatField(
        default=0
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return f"{self.user} - {self.plant}"