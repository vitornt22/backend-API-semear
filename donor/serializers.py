from rest_framework import serializers

from missionary.models import Missionary
from missionary.serializers import MissionarySerializer
from project.followerserializer import FollowerSerializer
from project.models import Follower, Project
from project.serializers import ProjectSerializer
from user.models import Information, UserModel
from user.serializers import InformationSerializer, UserSerializer

from .models import Donor


class UserCategoryDataSerializer (serializers.ModelSerializer):
    infomation = serializers.SerializerMethodField(
        'get_information')
    project = serializers.SerializerMethodField(
        'get_project')
    missionary = serializers.SerializerMethodField(
        'get_missionary')

    class Meta:
        model = UserModel
        fields = '__all__'

    def get_information(self, obj):
        informations = Information.objects.get(user=obj.id)
        return InformationSerializer(informations).data

    def get_project(self, obj):
        user = UserModel.objects.get(id=obj.id_user)
        try:
            if user.category == 'project':
                result = Project.objects.get(user=obj.user)
                return ProjectSerializer(result).data
            else:
                return None

        except Project.DoesNotExist:
            return None

    def get_missionary(self, obj):
        user = UserModel.objects.get(id=obj.id_user)

        try:
            if user.category == 'missionary':
                result = Missionary.objects.get(user=obj.user)
                return MissionarySerializer(result).data
            else:
                return None
        except Missionary.DoesNotExist:
            return None


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
