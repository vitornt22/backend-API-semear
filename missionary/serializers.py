from church.serializers import ChurchSerializer
from informations.serializers import AdressSerializer
from project.followerserializer import FollowerSerializer
from project.models import Follower
from rest_framework import serializers
from user.serializers import InformationSerializer, UserSerializer

from .models import Missionary


class MissionarySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    adress = AdressSerializer(allow_null=True, required=False)
    church = ChurchSerializer(allow_null=True, required=False)
    information = InformationSerializer()
    following = serializers.SerializerMethodField(
        'get_following')
    followers = serializers.SerializerMethodField(
        'get_followers')

    def get_following(self, obj):
        user = obj.user.id
        following = Follower.objects.filter(
            user=user)
        return FollowerSerializer(following, many=True).data

    def get_followers(self, obj):
        project = obj.id
        following = Follower.objects.filter(
            user2=project)
        return FollowerSerializer(following, many=True).data

    class Meta:
        model = Missionary
        fields = '__all__'
