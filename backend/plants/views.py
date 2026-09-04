from rest_framework.generics import ListAPIView
from django.db.models import Q

from .models import Plant
from .serializers import PlantSerializer



class PlantListAPIView(ListAPIView):

    serializer_class = PlantSerializer


    def get_queryset(self):

        queryset = Plant.objects.all()

        search = self.request.query_params.get(
            "search"
        )


        if search:

            queryset = queryset.filter(
                Q(name__icontains=search)
                |
                Q(scientific_name__icontains=search)
                |
                Q(family__icontains=search)
            )


        return queryset