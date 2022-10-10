# flake8: noqa: E501
from project.followerserializer import FollowerSerializer
from project.models import Follower
from publication.models import PublicationSaved
from publication.publicationSavedSerializer import PublicationSavedSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Information, UserModel


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField('get_followers')
    following = serializers.SerializerMethodField('get_following')
    savesPublications = serializers.SerializerMethodField(
        'get_saved_publications')

    def get_saved_publications(self, obj):
        publications = PublicationSaved.objects.filter(user=obj.id)
        return PublicationSavedSerializer(publications, many=True).data

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
                  'category', 'can_post', 'password', 'followers', 'savesPublications', 'following')
        extra_kwargs = {'password': {'write_only': True}}
