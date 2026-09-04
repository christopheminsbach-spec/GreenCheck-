from rest_framework.views import APIView  # type: ignore[import-not-found]
from rest_framework.response import Response  # type: ignore[import-not-found]
from django.contrib.auth.models import User  # type: ignore[import-not-found]


class RegisterView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        user = User.objects.create_user(
            username=username,
            password=password
        )

        return Response(
            {
                "message": "Utilisateur créé"
            }
        )