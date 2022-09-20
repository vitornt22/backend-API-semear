from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Missionary


class MissionarySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    id_adress = serializers.IntegerField(required=False, null=True, blank=True)
    church = serializers.IntegerField(required=False, null=True, blank=True)

    class Meta:
        model = Missionary
        fields = '__all__'
