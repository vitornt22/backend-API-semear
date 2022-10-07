from project.followerserializer import FollowerSerializer
from project.models import Follower
from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Donor


class DonorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    following = serializers.SerializerMethodField(
        'get_following')

    def get_following(self, obj):
        user = obj.user.id
        following = Follower.objects.filter(
            user=user)
        return FollowerSerializer(following, many=True).data

    class Meta:
        model = Donor
        fields = ('user', 'fullName', 'following')
