from informations.serializers import (AdressSerializer, BankDataSerializer,
                                      PIXSerializer)
from project.followerserializer import FollowerSerializer
from project.models import Follower
from rest_framework import serializers
from user.serializers import InformationSerializer, UserSerializer

from .models import Church


class ChurchSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    adress = AdressSerializer()
    bankData = BankDataSerializer()
    pix = PIXSerializer()
    information = InformationSerializer()
    following = serializers.SerializerMethodField(
        'get_following')

    class Meta:
        model = Church
        fields = '__all__'

    def get_following(self, obj):
        user = obj.user.id
        following = Follower.objects.filter(
            user=user)
        return FollowerSerializer(following, many=True).data
