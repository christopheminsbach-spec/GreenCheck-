from django.contrib import admin  # type: ignore[import-not-found,import-untyped]
from django.conf import settings  # type: ignore[import-not-found,import-untyped]
from django.conf.urls.static import static  # type: ignore[import-not-found,import-untyped]
from django.urls import include, path  # type: ignore[import-not-found,import-untyped]


from rest_framework_simplejwt.views import (  # type: ignore[import-not-found,import-untyped]
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "api/auth/",
        include("accounts.urls")
    ),

    path(
        "api/plants/",
        include("plants.urls")
    ),

    path(
        "api/",
        include("diagnostics.urls")
    ),
    path(
        "api/dashboard/",
        include("dashboard.urls")
    )


]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
