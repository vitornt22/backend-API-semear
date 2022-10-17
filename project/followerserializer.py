from church.models import Church
from donor.models import Donor
from missionary.models import Missionary
from rest_framework import serializers
from user.models import UserModel

from project.models import Project

from .extraSerializer import (ChurchSerializer, DonorSerializer,
                              MissionarySerializer, ProjectSerializer,
                              UserSerializer)
from .models import Follower


def get_category_data(user):
    if user.category == 'project':
        project = Project.objects.get(user=user)
        return ProjectSerializer(project).data
    elif user.category == 'church':
        church = Church.objects.get(user=user)
        return ChurchSerializer(church).data
    elif user.category == 'missionary':
        missionary = Missionary.objects.get(user=user)
        return MissionarySerializer(missionary).data
    elif user.category == 'donor':
        donor = Donor.objects.get(user=user)
        return DonorSerializer(donor).data


def return_user_data(pk):
    user = UserModel.objects.get(id=pk.id)
    return UserSerializer(user).data


class FollowerSerializer(serializers.ModelSerializer):
    userData = serializers.SerializerMethodField('get_user_data')
    user2Data = serializers.SerializerMethodField('get_user2_data')
    user = serializers.SerializerMethodField('get_user')
    user2 = serializers.SerializerMethodField('get_user2')

    class Meta:
        model = Follower
        fields = ['id', 'user', 'user2',
                  'userData', 'user2Data', 'created_at', 'updated_at']

    def get_user(self, obj):
        return return_user_data(obj.user)

    def get_user2(self, obj):
        return return_user_data(obj.user2)

    def get_user_data(self, obj):
        return get_category_data(obj.user)

    def get_user2_data(self, obj):
        return get_category_data(obj.user2)
