from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Donor


class DonorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Donor
        fields = ('user', 'fullName')
