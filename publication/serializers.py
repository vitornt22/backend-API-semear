

from project.serializers import ProjectSerializer
from rest_framework import serializers

from .models import Comment, Like, Publication


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(allow_null=True)
    likes = serializers.SerializerMethodField(
        'get_likes')
    comments = serializers.SerializerMethodField(
        'get_comments')

    class Meta:
        model = Publication
        fields = '__all__'

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
