from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):

    plants_count = serializers.IntegerField()

    identifications_count = serializers.IntegerField()

    users_count = serializers.IntegerField()

    latest_plants = serializers.ListField()