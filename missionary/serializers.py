from church.serializers import ChurchSerializer
from informations.serializers import AdressSerializer
from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Missionary


class MissionarySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    adress = AdressSerializer(allow_null=True, required=False)
    church = ChurchSerializer(allow_null=True, required=False)

    class Meta:
        model = Missionary
        fields = '__all__'
