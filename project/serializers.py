from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Project
        fields = '__all__'
