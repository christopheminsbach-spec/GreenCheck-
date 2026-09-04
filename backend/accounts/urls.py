from django.urls import path  # type: ignore[reportMissingModuleSource]
from rest_framework_simplejwt.views import TokenObtainPairView  # type: ignore[reportMissingImports]

from .views import RegisterView


urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login"
    ),
    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),
]