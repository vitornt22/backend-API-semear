from church.serializers import ChurchSerializer
from informations.serializers import AdressSerializer
from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Follower, Project


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    adress = AdressSerializer(allow_null=True, required=False)
    church = ChurchSerializer(allow_null=True, required=False)
    following = serializers.SerializerMethodField('get_following')
    followers = serializers.SerializerMethodField('get_followers')

    class Meta:
        model = Project
        fields = '__all__'

    def get_following(self, obj):
        user = obj.user.id
        following = Follower.objects.filter(
            user=user)
        return FollowerSerializer(following, many=True).data

    def get_followers(self, obj):
        project = obj.id
        following = Follower.objects.filter(
            project=project)
        return FollowerSerializer(following, many=True).data
