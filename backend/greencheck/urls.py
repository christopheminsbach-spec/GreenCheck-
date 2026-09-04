from django.contrib import admin  # pyright: ignore[reportMissingModuleSource]
from django.urls import path, include  # pyright: ignore[reportMissingModuleSource]

from drf_spectacular.views import (  # pyright: ignore[reportMissingImports]
    SpectacularAPIView,
    SpectacularSwaggerView,
)


urlpatterns=[


path(

"admin/",

admin.site.urls

),



path(

"api/",

include("plants.urls")

),



# Swagger JSON

path(

"api/schema/",

SpectacularAPIView.as_view(),

name="schema"

),



# Swagger UI

path(

"api/docs/",

SpectacularSwaggerView.as_view(

url_name="schema"

),

name="swagger-ui"

),


]