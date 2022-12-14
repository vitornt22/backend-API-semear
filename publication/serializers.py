

from rest_framework import serializers

from missionary.models import Missionary
from missionary.serializers import MissionarySerializer
from project.models import Project
from project.serializers import ProjectSerializer
from user.models import UserModel
from user.serializers import UserSerializer

from .models import Comment, Like, Publication, PublicationSaved


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(allow_null=True)
    project = serializers.SerializerMethodField(
        'get_project')
    missionary = serializers.SerializerMethodField(
        'get_missionary')
    likes = serializers.SerializerMethodField(
        'get_likes')
    comments = serializers.SerializerMethodField(
        'get_comments')

    class Meta:
        model = Publication
        fields = '__all__'

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

    def get_likes(self, obj):
        id = obj.id
        likes = Like.objects.filter(
            publication=id)
        return LikeSerializer(likes, many=True).data

    def get_comments(self, obj):
        id = obj.id
        comments = Comment.objects.filter(
            publication=id)
        return CommentSerializer(comments, many=True).data
