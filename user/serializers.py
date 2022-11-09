# flake8: noqa: E501
from nis import cat

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from project.followerserializer import FollowerSerializer
from project.models import Follower

from .get_category_information import get_category_information
from .models import Information, UserModel


class ValidationSerializer(serializers.Serializer):
    categoryData = serializers.SerializerMethodField('get_data')

    class Meta:
        fields = ('categoryData')

    def get_data(self, obj):
        return get_category_information(obj.category, obj.id)


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    information = serializers.SerializerMethodField('get_information')

    def get_information(self, obj):
        return get_category_information(obj.category, obj.id)

    def get_following(self, obj):
        user = obj.id
        following = Follower.objects.filter(
            user=user)
        return FollowerSerializer(following, many=True).data

    def get_followers(self, obj):
        if obj.category == 'project' or obj.category == 'missionary':
            user = obj.id
            following = Follower.objects.filter(
                user2=user)
            return FollowerSerializer(following, many=True).data
        else:
            return None

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email',
                  'category', 'can_post', 'password', 'information', 'created_at')
