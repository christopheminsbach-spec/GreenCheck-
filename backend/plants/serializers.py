from rest_framework import serializers

from .models import Plant


class PlantSerializer(serializers.ModelSerializer):

    class Meta:

        model = Plant

        fields = [
            "id",
            "name",
            "scientific_name",
            "family",
            "origin",
            "description",
            "care",
            "image_url",
        ]