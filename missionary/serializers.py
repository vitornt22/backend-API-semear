from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Missionary


class MissionarySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Missionary
        fields = '__all__'
