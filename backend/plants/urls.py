from django.urls import path  # type: ignore[reportMissingModuleSource]

from .views import PlantListAPIView


urlpatterns = [

    path(
        "",
        PlantListAPIView.as_view(),
        name="plants-list"
    ),

]