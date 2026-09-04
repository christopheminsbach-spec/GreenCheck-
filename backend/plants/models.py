from django.db import models


class Plant(models.Model):

    name = models.CharField(
        max_length=200
    )

    scientific_name = models.CharField(
        max_length=200,
        blank=True
    )

    family = models.CharField(
        max_length=200,
        blank=True
    )

    origin = models.CharField(
        max_length=200,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    care = models.TextField(
        blank=True
    )

    image_url = models.URLField(
    blank=True,
    null=True
)


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.name