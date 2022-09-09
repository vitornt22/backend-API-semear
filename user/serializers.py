# flake8: noqa: E501
from rest_framework import serializers

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email',
                  'category', 'can_post', 'password')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email',
                  'category', 'can_post', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserModel.objects.create_superuser(
            validated_data['category'], validated_data['username'], validated_data['can_post'], validated_data['email'], validated_data['password'])

        return user
