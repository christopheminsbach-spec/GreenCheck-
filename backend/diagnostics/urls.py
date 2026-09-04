from django.urls import path  # pyright: ignore[reportMissingModuleSource]
from .views import DiagnoseView


urlpatterns = [

    path(
        "diagnose/",
        DiagnoseView.as_view()
    )

]