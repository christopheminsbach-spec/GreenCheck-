import requests

from rest_framework.views import APIView  # type: ignore[import-not-found]
from rest_framework.response import Response  # type: ignore[import-not-found]



class DiagnoseView(APIView):


    def post(self,request):

        image=request.FILES.get("image")


        if not image:

            return Response(
                {
                    "error":"Image obligatoire"
                },
                status=400
            )


        response=requests.post(

            "http://localhost:8001/predict",

            files={
                "image":image
            }

        )


        return Response(
            response.json()
        )