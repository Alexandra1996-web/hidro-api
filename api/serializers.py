from rest_framework import serializers
from api.models import Auto


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ['id', 'marca', 'modelo', 'chapa']