from rest_framework.views import APIView
from rest_framework.response import Response

from plants.models import Plant
from identification.models import Identification

from django.contrib.auth.models import User



class DashboardAPIView(APIView):

    def get(self, request):

        latest_plants = Plant.objects.all().order_by(
            "-id"
        )[:5]


        plants = []

        for plant in latest_plants:

            plants.append({

                "id": plant.id,

                "name": plant.name,

                "scientific_name": plant.scientific_name

            })


        return Response({

            "plants_count":
                Plant.objects.count(),

            "identifications_count":
                Identification.objects.count(),

            "users_count":
                User.objects.count(),

            "latest_plants":
                plants

        })