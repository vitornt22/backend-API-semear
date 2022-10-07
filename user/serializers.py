# flake8: noqa: E501
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Information, UserModel


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email',
                  'category', 'can_post', 'password')
        extra_kwargs = {'password': {'write_only': True}}
