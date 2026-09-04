from rest_framework.views import APIView  # type: ignore[reportMissingImports]

from rest_framework.response import Response  # type: ignore[reportMissingImports]

from rest_framework.permissions import IsAuthenticated  # type: ignore[reportMissingImports]

from .serializers import RegisterSerializer



class RegisterAPIView(APIView):


    def post(self, request):


        serializer = RegisterSerializer(
            data=request.data
        )


        if serializer.is_valid():


            serializer.save()


            return Response(

                {
                "message":
                "Compte créé"
                },

                status=201

            )


        return Response(

            serializer.errors,

            status=400

        )





class ProfileAPIView(APIView):


    permission_classes=[

        IsAuthenticated

    ]



    def get(self,request):


        return Response({

            "username":
            request.user.username,


            "email":
            request.user.email

        })
