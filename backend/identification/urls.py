from django.urls import path

from .views import IdentifyPlantAPIView



urlpatterns = [


    path(
        "identify/",
        IdentifyPlantAPIView.as_view()
    )


]