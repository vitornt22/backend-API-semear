from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Donor


class DonorSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = Donor
        fields = '__all__'
