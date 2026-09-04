from django.urls import path  # type: ignore[reportMissingModuleSource]

from rest_framework_simplejwt.views import (  # type: ignore[reportMissingImports]
    TokenObtainPairView,
    TokenRefreshView
)


from .views import RegisterAPIView, ProfileAPIView



urlpatterns=[


path(

"register/",

RegisterAPIView.as_view()

),



path(

"login/",

TokenObtainPairView.as_view()

),



path(

"token/refresh/",

TokenRefreshView.as_view()

),



path(

"profile/",

ProfileAPIView.as_view()

),


]