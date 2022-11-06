from rest_framework import serializers

from church.models import Church
from donor.models import Donor
from missionary.models import Missionary
from project.models import Project
from user.models import UserModel

from .extraSerializer import (ChurchSerializer, DonorSerializer,
                              MissionarySerializer, ProjectSerializer,
                              UserSerializer)
from .models import Follower


def get_category_data(user):
    if user.category == 'project':
        try:
            project = Project.objects.get(user=user)
            return ProjectSerializer(project).data
        except Project.DoesNotExist:
            return None
    elif user.category == 'church':
        try:
            church = Church.objects.get(user=user)
            return ChurchSerializer(church).data
        except Church.DoesNotExist:
            return None
    elif user.category == 'missionary':
        try:
            missionary = Missionary.objects.get(user=user)
            return MissionarySerializer(missionary).data
        except Missionary.DoesNotExist:
            return None
    elif user.category == 'donor':
        try:
            donor = Donor.objects.get(user=user)
            return DonorSerializer(donor).data
        except Donor.DoesNotExist:
            return None


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
