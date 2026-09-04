from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Identification
from .serializers import IdentificationSerializer



class IdentifyPlantAPIView(APIView):


    permission_classes = [
        IsAuthenticated
    ]



    def post(self,request):


        image = request.FILES.get(
            "image"
        )


        identification = Identification.objects.create(

            user=request.user,

            image=image,

            confidence=0

        )


        serializer = IdentificationSerializer(
            identification
        )


        return Response(
            serializer.data
        )