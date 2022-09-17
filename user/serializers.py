# flake8: noqa: E501
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email',
                  'category', 'can_post', 'password')
        extra_kwargs = {'password': {'write_only': True}}
