from rest_framework import serializers
from api.models import Hidrometrica


class HidrometricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hidrometrica
        fields = ['id', 'fecha', 'nivel']