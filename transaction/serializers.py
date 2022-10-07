
from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Donation


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    donor = UserSerializer()

    class Meta:
        model = Donation
        fields = '__all__'
