from rest_framework import serializers  # type: ignore[reportMissingImports]

from .models import Diagnostic



class DiagnosticSerializer(
    serializers.ModelSerializer
):


    class Meta:


        model = Diagnostic


        fields = "__all__"