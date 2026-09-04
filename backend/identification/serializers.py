from rest_framework import serializers

from .models import Identification



class IdentificationSerializer(serializers.ModelSerializer):


    class Meta:

        model = Identification

        fields = "__all__"