from informations.serializers import (AdressSerializer, BankDataSerializer,
                                      PIXSerializer)
from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Church


class ChurchSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    adress = AdressSerializer()
    bankData = BankDataSerializer()
    Pix = PIXSerializer()

    class Meta:
        model = Church
        fields = '__all__'
